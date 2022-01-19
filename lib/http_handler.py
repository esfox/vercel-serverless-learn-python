from http.server import BaseHTTPRequestHandler
import ast

from helpers import to_json

class HTTPHandler(BaseHTTPRequestHandler):
    def get_request_json(self):
        content_length = int(self.headers.get('Content-Length'))
        post_body_bytes = self.rfile.read(content_length)
        post_body_string = post_body_bytes.decode('utf-8')
        data = ast.literal_eval(post_body_string)
        return data

    def send_json(self, data):
        response = to_json(data)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(response)
