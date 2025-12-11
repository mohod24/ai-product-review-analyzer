import React from "react";

const formatKeyPoints = (text) => {
  if (!text) return null;
  return text.split("\n").map((line, index) => (
    <p key={index} style={{ margin: "4px 0" }}>
      {line}
    </p>
  ));
};

function AnalysisResult({ result }) {
  if (!result) return null;

  const sentimentClass = result.sentiment
    ? result.sentiment.toUpperCase()
    : "NEUTRAL";
  const confidencePercent = result.confidence
    ? (result.confidence * 100).toFixed(1)
    : "0";

  return (
    <div className={`card result-box ${sentimentClass}`}>
      <h3 style={{ marginTop: 0, textAlign: "center" }}>
        🔍 Hasil Analisis AI
      </h3>

      <div
        className="result-header"
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          marginBottom: "1rem",
          textAlign: "center",
        }}
      >
        <div style={{ fontSize: "1.2rem", marginBottom: "5px" }}>
          <strong>Produk:</strong> {result.product_name}
        </div>

        <div className={`badge ${sentimentClass}`}>
          {sentimentClass} ({confidencePercent}%)
        </div>
      </div>
      {/* BATAS UPDATE */}

      <hr style={{ margin: "1rem 0", opacity: 0.3 }} />

      <div style={{ textAlign: "left" }}>
        <strong>💡 Poin-Poin Penting (by Gemini):</strong>
        <div style={{ marginTop: "0.5rem", lineHeight: "1.6" }}>
          {formatKeyPoints(result.key_points)}
        </div>
      </div>
    </div>
  );
}

export default AnalysisResult;
