def includeme(config):
    """
    Fungsi ini akan dipanggil otomatis oleh config.include('.routes')
    di __init__.py untuk mendaftarkan semua URL endpoint.
    """
    # Endpoint utama
    config.add_route('analyze', '/api/analyze')  # POST: Analisa review
    config.add_route('reviews', '/api/reviews')  # GET: Ambil history
    
    config.add_route('options_cors', '/api/{match:.*}')