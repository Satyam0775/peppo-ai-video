import os
import uuid
from fastapi import FastAPI, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from generate import generate_ai_video, generate_mock, USE_AI

app = FastAPI()

# Allow frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Ensure videos/ exists
os.makedirs("videos", exist_ok=True)

# ✅ Health check route
@app.get("/")
async def root():
    return {"status": "ok", "message": "Peppo AI backend is running!"}


@app.post("/generate")
async def generate_video(request: Request, prompt: str = Form(...)):
    """
    Generate video from prompt.
    - In cloud (Render free): returns mock sample.mp4
    - In Colab/local GPU: generates real AI video
    """
    output_name = f"{uuid.uuid4()}.mp4"
    output_path = f"videos/{output_name}"

    try:
        if USE_AI:
            generate_ai_video(prompt, output_path)
        else:
            generate_mock(prompt, output_path)
    except Exception as e:
        print("⚠️ Error, fallback to mock:", e)
        generate_mock(prompt, output_path)

    # ✅ Build full URL dynamically (important for Vercel frontend)
    base_url = str(request.base_url).rstrip("/")
    return {"video_url": f"{base_url}/videos/{output_name}"}


@app.get("/videos/{filename}")
async def serve_video(filename: str):
    """Serve generated or mock video"""
    return FileResponse(f"videos/{filename}")
