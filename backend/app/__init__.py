from pyramid.config import Configurator
from pyramid.events import NewRequest
from .models import init_db

def add_cors_headers_response_callback(event):
    """Menambahkan header CORS ke setiap response"""
    def cors_headers(request, response):
        response.headers.update({
        'Access-Control-Allow-Origin': '*', 
        'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
        'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Authorization',
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Max-Age': '1728000',
        })
    event.request.add_response_callback(cors_headers)

def main(global_config, **settings):
    """Fungsi utama aplikasi"""
    
    # 1. Inisialisasi Database
    init_db()

    with Configurator(settings=settings) as config:
        # 2. Setup CORS
        config.add_subscriber(add_cors_headers_response_callback, NewRequest)
        
        # 3. Include Routes dari file routes.py (REVISI DI SINI)
        # Ini akan menjalankan fungsi 'includeme' di dalam routes.py
        config.include('.routes')
        
        # 4. Scan views untuk menghubungkan route dengan fungsi logic-nya
        config.scan('.views')
        
        return config.make_wsgi_app()