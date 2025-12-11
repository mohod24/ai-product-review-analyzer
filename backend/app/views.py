import os
import google.generativeai as genai
from pyramid.view import view_config
from pyramid.response import Response
from .models import Review, DBSession
from dotenv import load_dotenv
import transaction

# --- LIBRARY PIPELINE ---
from transformers import pipeline

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

print("Sedang memuat model AI Sentiment... (Mohon tunggu sebentar)")
try:
    sentiment_pipeline = pipeline(
        task="text-classification",
        model="distilbert-base-uncased-finetuned-sst-2-english",
        return_all_scores=True
    )
    print("Model AI Sentiment berhasil dimuat!")
except Exception as e:
    print(f"Gagal memuat model: {e}")
    sentiment_pipeline = None


# --- HELPER FUNCTIONS ---

def analyze_sentiment_local(text):
    """Menggunakan Pipeline Lokal untuk analisis sentimen"""
    if not sentiment_pipeline:
        return "ERROR_MODEL", 0.0
    
    try:
        text = text[:512]
        
        results = sentiment_pipeline(text)
        
        first_output = results[0]
        top_result = max(first_output, key=lambda x: x['score'])
        
        label = top_result['label'].upper()
        score = top_result['score']
        
        return label, score
        
    except Exception as e:
        print(f"Error Pipeline: {e}")
        return "ERROR_PROCESS", 0.0

def extract_key_points_gemini(text):
    """Memanggil Gemini API (Tetap sama)"""
    try:
        model = genai.GenerativeModel('gemini-2.5-flash') 
        prompt = f"Analyze this product review and extract key points in simple bullet points. Review: '{text}'"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error Gemini: {e}")
        return "Failed to extract key points."

# --- API ENDPOINTS ---

@view_config(route_name='analyze', renderer='json', request_method='POST')
def analyze_review(request):
    try:
        data = request.json_body
        product_name = data.get('product_name')
        review_text = data.get('review_text')

        if not product_name or not review_text:
            request.response.status = 400
            return {'error': 'Product name and review text are required'}

        sentiment_label, confidence_score = analyze_sentiment_local(review_text)

        key_points_result = extract_key_points_gemini(review_text)

        new_review = Review(
            product_name=product_name,
            review_text=review_text,
            sentiment=sentiment_label,
            confidence=confidence_score,
            key_points=key_points_result
        )
        
        DBSession.add(new_review)
        transaction.commit()

        return {
            'message': 'Success',
            'data': new_review.to_dict()
        }

    except Exception as e:
        request.response.status = 500
        return {'error': str(e)}

@view_config(route_name='reviews', renderer='json', request_method='GET')
def get_reviews(request):
    try:
        reviews = DBSession.query(Review).order_by(Review.created_at.desc()).all()
        return [r.to_dict() for r in reviews]
    except Exception as e:
        request.response.status = 500
        return {'error': str(e)}

# Handle CORS
@view_config(route_name='analyze', request_method='OPTIONS')
@view_config(route_name='reviews', request_method='OPTIONS')
@view_config(route_name='options_cors', request_method='OPTIONS')
def cors_options(request):
    return Response(status=200)