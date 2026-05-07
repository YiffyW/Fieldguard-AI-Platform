"""
FieldGuard AI — static file server
Run: python server.py
Opens http://localhost:8000
"""
import http.server, socketserver, webbrowser, os

PORT = 8000
ROOT = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def end_headers(self):
        # Allow fetch() from same origin; no CORS issues for local use
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def log_message(self, fmt, *args):
        print(f"  {self.address_string()} → {fmt % args}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    url = f"http://localhost:{PORT}/index.html"
    print(f"FieldGuard AI server running at {url}")
    print("Press Ctrl+C to stop.\n")
    webbrowser.open(url)
    httpd.serve_forever()
