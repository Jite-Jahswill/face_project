# 🚀 Face Recognition Web App

A **fully browser-based** face recognition system that lets users **register** and **recognize** faces in real time using just a webcam — no app installation required!

Built with **Flask** (Python backend) + **pure HTML/JavaScript** (frontend). Uses **DeepFace** for state-of-the-art face recognition and the **Web Speech API** to speak the recognized name aloud.

Works perfectly on **desktop and mobile** (iPhone/Android) via local network or public URL.

![demo](https://img.shields.io/badge/status-working-brightgreen) ![mobile](https://img.shields.io/badge/mobile-friendly-blue) ![python](https://img.shields.io/badge/Python-3.9%2B-blue)

---

### ✨ Features

- 📸 **Register New Users** – Take a photo via webcam and save with name
- 🧠 **Real-time Face Recognition** – Instantly detects and identifies known faces
- 🔊 **Voice Announcement** – Browser speaks: _"This is John Doe"_
- 🗂️ **Local Face Database** – Images + metadata stored in `known/` folder
- 🌐 **Mobile Friendly** – Works on phones (with HTTPS via ngrok)
- ⚡ **Zero Client Dependencies** – Pure browser experience

---

### 📁 Project Structure

```
face_project/
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
├── static/
│   └── index.html          # Frontend UI (pure HTML + JS)
├── known/                  # Registered face images (.jpg)
├── metadata.json           # Name mappings for recognized faces
└── README.md               # You are here ✨
```

---

### 🛠️ Local Development Setup

```bash
# 1. Clone the repo
git clone https://github.com/Jite-Jahswill/face_project.git
cd face_project

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
python app.py
```

Server runs at: 👉 http://localhost:5001

Your local IP will also be shown (e.g., `http://192.168.1.105:5001`) — use this to access from your phone on the same Wi-Fi.

---

### 📱 Access from Mobile (iPhone/Android)

iOS blocks camera access on HTTP. Use **ngrok** for HTTPS:

```bash
ngrok http 5001
```

Copy the `https://xxxx.ngrok.io` URL and open it on your phone → full webcam access!

---

### 👤 How to Use

#### Register a New User
1. Click **"Register User"**
2. Enter your name
3. Allow camera → smile! 📸
4. Success! Your face is saved as `known/Your_Name.jpg`

#### Recognize Faces
1. Click **"Start Recognition"**
2. Look at the camera
3. When recognized:
   - Name appears on screen
   - You hear: **"This is [Your Name]"**

---

### 🚀 Deploy on Render (Free Hosting)

1. Push your code to GitHub
2. Go to [https://render.com](https://render.com)
3. New → **Web Service** → Connect your GitHub repo
4. Settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
5. Deploy!

You’ll get a live URL like:  
https://face-recog.onrender.com

> Optional: I can provide a Render-optimized `index.html` that auto-detects the backend URL.

---

### 📦 Requirements

- Python 3.9+
- Flask
- DeepFace
- OpenCV
- face_recognition (or DeepFace built-in models)

All dependencies are in `requirements.txt`

---

### 🔮 Upcoming / Optional Features (on request)

- [ ] Live demo badge
- [ ] Screenshots / GIF demo in README
- [ ] Dockerfile for Docker deployment
- [ ] Render/Gunicorn optimized config
- [ ] Multiple face support in one frame

Just ask — I’ll add them instantly!

---

### 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

### 📜 License

[MIT License](LICENSE) – free to use, modify, and distribute.

---

Made with ❤️ by [Jite Jahswill](https://github.com/Jite-Jahswill)

⭐ **Star this repo if you found it useful!**
