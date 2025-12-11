import { useEffect, useState } from "react";
import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:6543/api";

function ReviewList({ refreshTrigger }) {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    fetchReviews();
  }, [refreshTrigger]);

  const fetchReviews = async () => {
    try {
      const response = await axios.get(`${API_URL}/reviews`);
      setReviews(response.data);
    } catch (error) {
      console.error("Error fetching history:", error);
    }
  };

  return (
    <div className="card">
      <h2>📚 Riwayat Analisis</h2>
      {reviews.length === 0 ? (
        <p style={{ textAlign: "center", color: "#888" }}>
          Belum ada data review.
        </p>
      ) : (
        <div>
          {reviews.map((review) => (
            <div key={review.id} className="history-item">
              <div style={{ display: "flex", justifyContent: "space-between" }}>
                <strong>{review.product_name}</strong>
                <span className={`badge ${review.sentiment}`}>
                  {review.sentiment}
                </span>
              </div>
              <p style={{ fontSize: "0.9rem", color: "#555", margin: "5px 0" }}>
                {review.review_text.substring(0, 80)}...
              </p>
              <small style={{ color: "#aaa" }}>
                {new Date(review.created_at).toLocaleString()}
              </small>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default ReviewList;
