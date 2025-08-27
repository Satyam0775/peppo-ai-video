import { useState } from "react";
import axios from "axios";

function App() {
  const [prompt, setPrompt] = useState("");
  const [videoUrl, setVideoUrl] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!prompt) return alert("Please enter a prompt!");

    const formData = new FormData();
    formData.append("prompt", prompt);

    try {
      setLoading(true);
      const API_URL = import.meta.env.VITE_API_URL;

      const res = await axios.post(`${API_URL}/generate`, formData);
      console.log("Backend response:", res.data);

      let videoPath = res.data.video_url;
      if (!videoPath.startsWith("http")) {
        videoPath = `${API_URL}${videoPath}`;
      }

      setVideoUrl(videoPath);
    } catch (err) {
      console.error("Error generating video:", err);
      alert("Error generating video. Check backend logs.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: 20, fontFamily: "sans-serif" }}>
      <h1>🎬 Peppo AI Video Generator</h1>
      <input
        type="text"
        placeholder="Enter your prompt..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        style={{
          padding: 10,
          width: "60%",
          borderRadius: 5,
          border: "1px solid #ccc",
        }}
      />
      <button
        onClick={handleGenerate}
        style={{
          marginLeft: 10,
          padding: "10px 20px",
          borderRadius: 5,
          border: "none",
          background: "#4CAF50",
          color: "white",
          cursor: "pointer",
        }}
      >
        {loading ? "Generating..." : "Generate Video"}
      </button>

      {videoUrl && (
        <div style={{ marginTop: 20 }}>
          <h3>Generated Video:</h3>
          <video
            src={videoUrl}
            controls
            width="480"
            style={{ border: "1px solid #ddd", borderRadius: 8 }}
          ></video>
        </div>
      )}
    </div>
  );
}

export default App;
