#!/usr/bin/env python
from http.server import HTTPServer, CGIHTTPRequestHandler
import webbrowser

class Handler(CGIHTTPRequestHandler):
    cgi_directories = ["/cgi-bin"]

PORT = 8000

httpd = HTTPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
