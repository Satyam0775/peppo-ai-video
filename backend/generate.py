import os
import shutil
from pathlib import Path

# Flag: Enable AI only if USE_AI=true
USE_AI = os.getenv("USE_AI", "false").lower() == "true"

if USE_AI:
    import torch
    import imageio
    from diffusers import StableDiffusionPipeline, StableVideoDiffusionPipeline
    from PIL import Image

    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    print("🚀 Loading Stable Diffusion + Stable Video Diffusion...")
    txt2img = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5", torch_dtype=dtype
    ).to(device)

    vid_pipe = StableVideoDiffusionPipeline.from_pretrained(
        "stabilityai/stable-video-diffusion-img2vid",
        torch_dtype=dtype,
        variant="fp16" if torch.cuda.is_available() else None
    ).to(device)

    def generate_ai_video(prompt: str, output_path: str):
        """Generate real AI video (local/Colab with GPU)"""
        image = txt2img(prompt).images[0]
        result = vid_pipe(image, num_frames=48)  # ~9s @ 5fps
        frames = result.frames[0]
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        imageio.mimsave(output_path, frames, fps=5)
        return output_path
else:
    def generate_ai_video(prompt: str, output_path: str):
        """Disabled in Render deployment"""
        raise RuntimeError("AI mode disabled in cloud deployment")


def generate_mock(prompt: str, output_path: str):
    """Always safe fallback: copy sample.mp4"""
    shutil.copy("sample.mp4", output_path)
    return output_path
