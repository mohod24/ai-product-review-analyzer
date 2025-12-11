import os
from sqlalchemy import (
    Column,
    Integer,
    Text,
    String,
    Float,
    DateTime,
    create_engine,
)
from sqlalchemy.orm import  declarative_base, sessionmaker, scoped_session
from datetime import datetime
from dotenv import load_dotenv

# Load env variables dari file .env
load_dotenv()

# Setup Koneksi Database
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "review_analyzer_db")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

# Connection String PostgreSQL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# SQLAlchemy Setup
DBSession = scoped_session(sessionmaker())
Base = declarative_base()

# Definisi Tabel Review 
class Review(Base):
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True)
    product_name = Column(String(255), nullable=False)
    review_text = Column(Text, nullable=False)
    sentiment = Column(String(50)) # POSITIVE / NEGATIVE / NEUTRAL
    confidence = Column(Float)     # Score 0.0 - 1.0
    key_points = Column(Text)      # Hasil ringkasan dari Gemini
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Helper untuk convert object ke JSON"""
        return {
            "id": self.id,
            "product_name": self.product_name,
            "review_text": self.review_text,
            "sentiment": self.sentiment,
            "confidence": self.confidence,
            "key_points": self.key_points,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }

def init_db():
    """Fungsi untuk inisialisasi tabel di database"""
    engine = create_engine(DATABASE_URL)
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    return engine