import http.server
import socketserver
import subprocess
import os

PORT = 3000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving HTTP at port", PORT)
    httpd.serve_forever()
