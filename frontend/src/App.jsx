import { useState } from "react";
import "./App.css";
import ReviewForm from "./components/ReviewForm";
import AnalysisResult from "./components/AnalysisResult";
import ReviewList from "./components/ReviewList";

function App() {
  const [latestResult, setLatestResult] = useState(null);
  const [refreshHistory, setRefreshHistory] = useState(0);

  const handleAnalysisComplete = (result) => {
    setLatestResult(result);
    setRefreshHistory((prev) => prev + 1);
  };

  return (
    <div className="container">
      <h1>AI Product Review Analyzer</h1>
      <h2>Alief Athallah - 123140184</h2>
      <p style={{ textAlign: "center", marginBottom: "2rem" }}>
        Powered by Hugging Face (Sentiment) & Google Gemini (Summary)
      </p>

      <ReviewForm onAnalysisComplete={handleAnalysisComplete} />

      <AnalysisResult result={latestResult} />

      <ReviewList refreshTrigger={refreshHistory} />
    </div>
  );
}

export default App;
