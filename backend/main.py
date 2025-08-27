import os
import uuid
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from generate import generate_ai_video, generate_mock, USE_AI

app = FastAPI()

# Allow frontend (Vercel) to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate_video(prompt: str = Form(...)):
    output_name = f"{uuid.uuid4()}.mp4"
    output_path = f"videos/{output_name}"

    try:
        if USE_AI:
            generate_ai_video(prompt, output_path)
        else:
            generate_mock(prompt, output_path)
    except Exception as e:
        print("⚠️ Error, falling back to mock:", e)
        generate_mock(prompt, output_path)

    return {"video_url": f"/videos/{output_name}"}


@app.get("/videos/{filename}")
async def serve_video(filename: str):
    return FileResponse(f"videos/{filename}")
