# 🎬 Peppo AI Video Generator

## 📌 Overview
This project is built for the **Peppo AI Engineering Internship Challenge**.  

- Takes a **text prompt** from the frontend  
- Generates a **short video (5–10 seconds)** using AI (Stable Video Diffusion) if GPU is available  
- Returns and displays the video in the browser  
- For deployment (no GPU available), the backend falls back to a **sample.mp4** mock video  

✅ This ensures the app always works on public cloud, while still demonstrating real AI text-to-video (T2V) capabilities locally/Colab.  

---

## 🛠️ Tech Stack
- **Frontend** → React (Vite)  
- **Backend** → FastAPI (Python)  
- **AI Models** → Stable Diffusion (txt2img) + Stable Video Diffusion (img2vid)  
- **Deployment** → Render (backend) + Vercel (frontend)  
- **Mock fallback** → `sample.mp4` for environments without GPU  

---

## 🚀 Live Demo
- **Frontend (Vercel)** → [Live Link Here](https://YOUR-FRONTEND-URL.vercel.app)  
- **Backend (Render)** → [Live Link Here](https://YOUR-BACKEND-URL.onrender.com)  

⚠️ **Note**: Deployed demo uses **mock mode** because Render/Vercel do not provide GPUs.  

---

## 🖥️ Local Development

### 1. Clone the repo
```bash
git clone https://github.com/Satyam0775/peppo-ai-video.git
cd peppo-ai-video
