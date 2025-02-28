import http.server
import socketserver
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import webbrowser
import threading
import time

# HTML injection for auto-reload functionality
RELOAD_SCRIPT = """
    <script>
        let socket = new WebSocket('ws://' + window.location.host.split(':')[0] + ':9001');
        socket.onmessage = function(event) {
            if (event.data === 'reload') {
                window.location.reload();
            }
        };
    </script>
</body>
"""

class AutoReloadHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        if self.path == '/':
            self.path = '/portfolio-website.html'
        return super().do_GET()

    def send_response(self, code, message=None):
        super().send_response(code, message)
        if code == 200 and self.path.endswith('.html'):
            self.send_header('Content-Type', 'text/html; charset=utf-8')

    def copyfile(self, source, outputfile):
        if self.path.endswith('.html'):
            content = source.read().decode('utf-8')
            modified_content = content.replace('</body>', RELOAD_SCRIPT)
            outputfile.write(modified_content.encode('utf-8'))
        else:
            super().copyfile(source, outputfile)

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.html'):
            print(f"File {event.src_path} has been modified")
            broadcast_reload()

import asyncio
import websockets

connected_clients = set()

async def register(websocket):
    connected_clients.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        connected_clients.remove(websocket)

async def websocket_server():
    async with websockets.serve(register, "localhost", 9001):
        await asyncio.Future()  # run forever

def broadcast_reload():
    if connected_clients:
        websockets.broadcast(connected_clients, "reload")

def run_websocket_server():
    asyncio.run(websocket_server())

def run_http_server():
    port = 8000
    handler = AutoReloadHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving at http://localhost:{port}")
        httpd.serve_forever()

if __name__ == "__main__":
    # Start WebSocket server in a separate thread
    websocket_thread = threading.Thread(target=run_websocket_server)
    websocket_thread.daemon = True
    websocket_thread.start()

    # Start file watcher
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    # Open the browser
    webbrowser.open('http://localhost:8000')

    # Start HTTP server
    try:
        run_http_server()
    except KeyboardInterrupt:
        observer.stop()
        observer.join() 