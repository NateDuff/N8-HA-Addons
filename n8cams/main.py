import http.server
import socketserver

PORT = 8000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hey there world from python!!") # Response body

# Create an HTTP server with custom request handler
with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print("Server running at port", PORT)
    httpd.serve_forever()
