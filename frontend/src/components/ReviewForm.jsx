import { useState } from "react";
import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:6543/api";

function ReviewForm({ onAnalysisComplete }) {
  const [productName, setProductName] = useState("");
  const [reviewText, setReviewText] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await axios.post(`${API_URL}/analyze`, {
        product_name: productName,
        review_text: reviewText,
      });

      onAnalysisComplete(response.data.data);

      setProductName("");
      setReviewText("");
    } catch (err) {
      console.error(err);
      setError("Gagal menganalisis review. Pastikan backend berjalan.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>📝 Input Review Produk</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Nama Produk:</label>
          <input
            type="text"
            value={productName}
            onChange={(e) => setProductName(e.target.value)}
            placeholder="Contoh: Laptop Gaming X1"
            required
          />
        </div>

        <div className="form-group">
          <label>Ulasan / Review:</label>
          <textarea
            value={reviewText}
            onChange={(e) => setReviewText(e.target.value)}
            placeholder="Tulis ulasan lengkap di sini..."
            required
          />
        </div>

        {error && <p style={{ color: "red" }}>{error}</p>}

        <button type="submit" disabled={loading}>
          {loading ? "Sedang Menganalisis (AI)..." : "Analisis Review"}
        </button>
      </form>
    </div>
  );
}

export default ReviewForm;
