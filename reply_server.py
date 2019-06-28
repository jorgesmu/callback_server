from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO


class ReplyPostRequestHandler(BaseHTTPRequestHandler):
    def __reply(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'Headers: ' + str.encode(str(self.headers)))
        response.write(b'Url: ' + str.encode(self.path))
        response.write(b'\n\r')
        response.write(b'Body: ' + str.encode(str(body)))
        self.wfile.write(response.getvalue())


    def do_POST(self):
        self.__reply()


    def do_GET(self):
        self.__reply()

PORT = 8000
httpd = HTTPServer(('localhost', 8000), ReplyPostRequestHandler)
print('Starting server at port: ', PORT)
httpd.serve_forever()