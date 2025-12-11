from wsgiref.simple_server import make_server
from app import main
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 6543))
    app = main({})
    print(f"Starting server on http://localhost:{port}")
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()