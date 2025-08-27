import torch
import imageio
from pathlib import Path
from diffusers import StableDiffusionPipeline, StableVideoDiffusionPipeline
from PIL import Image

# Try to load models
try:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    print("Loading Stable Diffusion (text-to-image)...")
    txt2img_pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5", torch_dtype=dtype
    ).to(device)

    print("Loading Stable Video Diffusion (image-to-video)...")
    vid_pipe = StableVideoDiffusionPipeline.from_pretrained(
        "stabilityai/stable-video-diffusion-img2vid",
        torch_dtype=dtype,
        variant="fp16" if torch.cuda.is_available() else None
    ).to(device)

    MODEL_READY = True
except Exception as e:
    print("⚠️ Model load failed:", e)
    txt2img_pipe, vid_pipe = None, None
    MODEL_READY = False


def generate_ai_video(prompt: str, output_path: str):
    """
    Generate a 5–10 sec AI video from text prompt.
    1. Create image from text
    2. Convert image → video frames
    3. Save as mp4
    """
    if not MODEL_READY:
        raise RuntimeError("AI models not available. Use mock instead.")

    # Step 1: Text → Image
    image = txt2img_pipe(prompt).images[0]

    # Step 2: Image → Video
    result = vid_pipe(image, num_frames=48)  # 48 frames @ 5fps ≈ 9.6 sec
    frames = result.frames[0]

    # Step 3: Save video
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    imageio.mimsave(output_path, frames, fps=5)  # 5fps
    return output_path


def generate_mock(prompt: str, output_path: str):
    """Fallback: copy sample.mp4 (for cloud deployment)."""
    import shutil
    shutil.copy("sample.mp4", output_path)
    return output_path
