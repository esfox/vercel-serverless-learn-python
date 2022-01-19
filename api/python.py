from lib.http_handler import HTTPHandler
from db import db

class handler(HTTPHandler):

    def do_GET(self):
        data = db.things.get_all()
        self.send_json(data)
        return

    def do_POST(self):
        data = self.get_request_json()
        data = db.things.create(data)
        self.send_json(data)
        return
