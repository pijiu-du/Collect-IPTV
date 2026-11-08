from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os

PORT = int(os.environ.get("PORT", 8080))

class Handler(SimpleHTTPRequestHandler):
    pass

with TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Collect-IPTV server running on port {PORT}")
    httpd.serve_forever()
