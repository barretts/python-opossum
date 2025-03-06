import http.server
import socketserver
from http import HTTPStatus

PORT = 8000

def add_cors_headers(handler):
    handler.send_header('Access-Control-Allow-Origin', 'http://localhost:3000')
    handler.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    handler.send_header('Access-Control-Allow-Headers', 'Content-Type')

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/data':
            # Handle API endpoint
            self.send_response(HTTPStatus.OK)
            add_cors_headers(self)
            self.send_header('Content-Type', 'application/json') 
            self.end_headers()
            
            # Send JSON response
            data = {"message": "Hello from Python!"}
            json_response = json.dumps(data).encode("utf-8")
            self.wfile.write(json_response)
        else:
            # Serve files normally (e.g., static HTML/JS assets)
            super().do_GET()

if __name__ == '__main__':
    server_address = ('', 8000)
    print(f"Server running on port {PORT}")
    http.server.HTTPServer(server_address, CustomHTTPRequestHandler).serve_forever()
