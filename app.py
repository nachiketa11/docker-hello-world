from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, World! Docker is working!")
    def log_message(self, *args):
        pass

print("Server running on port 8080...")
HTTPServer(("", 8080), Handler).serve_forever()