from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import uuid, os
from generate import generate_ai_video, generate_mock, MODEL_READY

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("videos", exist_ok=True)

@app.post("/generate")
async def generate_video(prompt: str = Form(...)):
    """
    Generate a video from text prompt.
    - If GPU + model available → AI generation
    - Otherwise → mock sample.mp4 fallback
    """
    output_name = f"{uuid.uuid4()}.mp4"
    output_path = os.path.join("videos", output_name)

    try:
        if MODEL_READY:
            generate_ai_video(prompt, output_path)
        else:
            generate_mock(prompt, output_path)
    except Exception as e:
        print("⚠️ Falling back to mock due to error:", e)
        generate_mock(prompt, output_path)

    return {"video_url": f"http://localhost:8000/videos/{output_name}"}


@app.get("/videos/{filename}")
async def serve_video(filename: str):
    return FileResponse(os.path.join("videos", filename))
