# https://stackoverflow.com/questions/21956683/enable-access-control-on-simple-http-server
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys

class XFrameRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('X-Frame-Options', 'sameorigin')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    test(XFrameRequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)