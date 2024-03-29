from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT = 8000

class WebRequestHandler(BaseHTTPRequestHandler):
    def get_response(self):
        return json.dumps(
            {
                "a": 1,
                "b": 2,
                "c": 3,
            }
        )
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(self.get_response().encode("utf-8"))

    def do_POST(self):
        self.do_GET()

if __name__ == "__main__":
    print(f"Starting server on port {PORT}")
    server = HTTPServer(("0.0.0.0", PORT), WebRequestHandler)
    server.serve_forever()
