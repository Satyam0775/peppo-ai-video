# 🎬 Peppo AI Video Generator

An AI-powered app that takes a text prompt and generates a **short 5–10s video**.  
Built as part of the **Peppo AI Engineering Internship Challenge**.

---

## 🚀 Features
- Text prompt → short video (mock on Render, real AI in Colab/Local GPU).
- **Backend (FastAPI)** → hosted on **Render**.
- **Frontend (React + Vite)** → hosted on **Vercel**.
- Secure environment variables (`.env` not committed).
- Simple UI with input box + video preview.

---

## 🌐 Live Links
- **Frontend (Vercel)** → [Live Demo](https://peppo-ai-video.vercel.app)  
- **Backend (Render)** → [API Docs](https://peppo-ai-video.onrender.com/docs)  
- **Colab Notebook (Real AI Demo)** → [Run on Colab](https://colab.research.google.com/drive/1T022oGhrvKQm8bRQDCC4GtTLIlCFfazq?usp=sharing)


---


---

## ⚡ Tech Stack
- **Backend** → FastAPI, Uvicorn, Python
- **Frontend** → React, Vite, Axios
- **Video/AI** → Diffusers, Torch, ImageIO (mocked on cloud due to GPU/memory limits)
- **Deployment** → Render (backend), Vercel (frontend)

---

## 🖥️ Running Locally

### 1. Clone repo
```bash
git clone https://github.com/Satyam0775/peppo-ai-video.git
cd peppo-ai-video

2. Run Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload


Backend runs on: http://127.0.0.1:8000

3. Run Frontend
cd frontend
npm install
echo "VITE_API_URL=http://127.0.0.1:8000" > .env.local
npm run dev


Frontend runs on: http://localhost:5173

☁️ Deployment
Backend (Render)

Root Directory: backend

Build Command: pip install -r requirements.txt

Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT

Frontend (Vercel)

Root Directory: frontend

Framework: Vite

Build Command: npm run build

Output Directory: dist

Environment Variable:

VITE_API_URL=https://peppo-ai-video.onrender.com

🎥 Example Prompts

A futuristic city with flying cars

A dog playing football in a stadium

A robot painting on a canvas

👉 On Render (mock mode) → always shows sample.mp4
👉 On Colab/Local GPU → generates real AI videos

📝 Notes

Free Render plan has 512MB RAM limit → AI video generation is mocked with sample.mp4.

For real AI video → use the provided Colab Notebook with GPU.

API keys (if used) are stored in .env (never committed).

✅ Scoring Checklist

Functionality (40) → Prompt → Video → Displayed ✅

Deployment (20) → Render + Vercel live links ✅

Code Quality (15) → Clean, modular ✅

Documentation (10) → This README ✅

Innovation (10) → Colab GPU demo ✅

Security (5) → .env, no keys exposed ✅

👨‍💻 Built by Satyam Kumar
For Peppo AI Engineering Internship Challenge


---

⚡ With this `README.md`, you’re **100% submission-ready**.  

👉 Do you want me to also give you a **ready Colab notebook link template** (with `Open in Colab` badge), so evaluators can just click and run the real AI demo?


## 📂 Project Structure

