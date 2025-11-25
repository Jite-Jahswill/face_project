from flask import Flask, request, jsonify, send_from_directory
import os, json, base64, re, cv2
from deepface import DeepFace
import numpy as np

app = Flask(__name__)
KNOWN_DIR = "known"
os.makedirs(KNOWN_DIR, exist_ok=True)
META_FILE = os.path.join(KNOWN_DIR, "metadata.json")

# Load metadata
if os.path.exists(META_FILE):
    with open(META_FILE) as f:
        metadata = json.load(f)
else:
    metadata = {}

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    image_data = data.get("image")
    name = data.get("name")

    if not image_data or not name:
        return jsonify({"message": "Image or name missing"}), 400

    try:
        img_str = re.sub(r"^data:image/.+;base64,", "", image_data)
        img_bytes = base64.b64decode(img_str)
        nparr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        user_id = name.replace(" ", "_")
        user_path = os.path.join(KNOWN_DIR, f"{user_id}.jpg")
        cv2.imwrite(user_path, img)

        metadata[user_id] = {"name": name}
        with open(META_FILE, "w") as f:
            json.dump(metadata, f, indent=2)

        return jsonify({"message": f"{name} registered successfully!"})
    except Exception as e:
        return jsonify({"message": f"Registration failed: {str(e)}"}), 500

@app.route("/recognize", methods=["POST"])
def recognize():
    data = request.get_json()
    image_data = data.get("image")

    if not image_data:
        return jsonify({"message": "Image missing"}), 400

    try:
        img_str = re.sub(r"^data:image/.+;base64,", "", image_data)
        img_bytes = base64.b64decode(img_str)
        nparr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        recognized_user = None
        for file in os.listdir(KNOWN_DIR):
            if file.endswith(".jpg"):
                db_img = cv2.imread(os.path.join(KNOWN_DIR, file))
                result = DeepFace.verify(img, db_img, enforce_detection=False)
                if result["verified"]:
                    user_id = file.replace(".jpg", "")
                    recognized_user = metadata[user_id]
                    break

        if recognized_user:
            return jsonify({"recognized": True, "user": recognized_user})
        else:
            return jsonify({"recognized": False})
    except Exception as e:
        return jsonify({"message": f"Recognition failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
