import http.server
import socketserver
import subprocess
import os

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

frpc_path = "./frpc"
os.chmod(frpc_path, 0o755)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving HTTP at port", PORT)
    httpd.serve_forever()

frpc_process = subprocess.Popen([frpc_path, "-c", "frpc.toml"])

frpc_process.wait()
