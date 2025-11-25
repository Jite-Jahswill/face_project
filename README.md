🚀 Face Recognition Web App

A full browser-based face recognition system that allows users to register and recognize faces dynamically using only a webcam. The backend runs on Flask, while the frontend uses pure HTML + JavaScript to capture images and send them to the server.

✨ Features

📸 Register New Users
Capture a face photo from the browser and save it to the backend.

🧠 Automatic Recognition
Shows the user’s name when recognized in live video feed.

🔊 Voice Output
Browser speaks the detected user's name aloud.

🗂️ Local Face Storage
Saved in known/ directory with metadata in metadata.json.

🌐 Mobile Friendly
Works on iPhone/Android using HTTPS tunneling (ngrok).

📁 Project Structure
face_project/
│
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── static/
│    └── index.html        # Frontend UI
│
├── known/                 # Stores registered face images
│    └── metadata.json     # Stores name info
│
└── README.md

🛠️ Installation (Local Development)
1. Clone Repo
git clone https://github.com/Jite-Jahswill/face_project.git
cd face_project

2. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Run Server
python app.py


App runs at:
👉 http://localhost:5001

📱 Access From Your Phone (iPhone/Android)

Local IP is shown when you run app:

* Running on http://192.168.x.x:5001


Visit that URL in your phone (same WiFi).

If camera is blocked on iPhone

Browsers require HTTPS for camera access.

Use ngrok:

ngrok http 5001


Use the https URL it gives you.

👤 Register a New User

Click Register User

Enter name

Take a webcam photo

A success modal appears

User photo is saved in:

known/<name>.jpg


Example:

known/Jite_Jahswill.jpg


Metadata saved in:

known/metadata.json

🔍 Face Recognition

Open Recognition Mode

App scans your face in live feed

When recognized, you hear:

“This is Jite Jahswill”

Name appears on screen

🌍 Deploy on Render
1. Push project to GitHub
git push --set-upstream origin main

2. Go to Render

https://render.com

3. Create New → Web Service
4. Select Your GitHub Repo
5. Set Environment:
Build Command: pip install -r requirements.txt
Start Command: python app.py


Render gives you a hosted URL like:

https://face-recog.onrender.com

6. Make frontend request correct backend URL

(If needed, I’ll update index.html for you.)

📦 Requirements

Python 3.9+

Flask

DeepFace

OpenCV

SpeechRecognition (frontend uses Web Speech API)

Everything is pre-configured in requirements.txt.

🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first.

📜 License

MIT License

If you want, I can also add:

✅ Render-specific configuration
✅ Dockerfile for containerized deployment
✅ Screenshots / GIF demo
✅ Live demo badge

Just tell me!
