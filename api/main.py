from http.server import BaseHTTPRequestHandler
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        current_dir = os.path.dirname(__file__)
        html_file_path = os.path.join(current_dir, 'html', 'index.html')
        with open(html_file_path, 'rb') as file:
            html_content = file.read()
        self.wfile.write(html_content)

def main(req, res):
    return handler(req, res)

