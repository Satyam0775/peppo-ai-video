import { useState } from "react";
import axios from "axios";

function App() {
  const [prompt, setPrompt] = useState("");
  const [videoUrl, setVideoUrl] = useState("");

  const handleGenerate = async () => {
    const formData = new FormData();
    formData.append("prompt", prompt);

    try {
      const res = await axios.post("http://localhost:8000/generate", formData);
      setVideoUrl(res.data.video_url);
    } catch (err) {
      console.error("Error generating video:", err);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>🎬 Peppo AI Video Generator</h1>
      <input
        type="text"
        placeholder="Enter your prompt..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        style={{ padding: 10, width: "60%" }}
      />
      <button onClick={handleGenerate} style={{ marginLeft: 10, padding: 10 }}>
        Generate Video
      </button>

      {videoUrl && (
        <div style={{ marginTop: 20 }}>
          <h3>Generated Video:</h3>
          <video src={videoUrl} controls width="480"></video>
        </div>
      )}
    </div>
  );
}

export default App;
 
