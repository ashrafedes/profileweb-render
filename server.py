#!/usr/bin/env python3
"""
Local development server with write support.
Serves static files AND allows the dashboard to write files (articles.json, sitemap.xml, rss.xml)
directly to disk via POST requests — no downloads, no folder pickers.

Usage: python server.py
Then open: http://localhost:8080/articles/dashboard.html
"""

import http.server
import json
import os
import urllib.parse

PORT = 8080
ROOT = os.path.dirname(os.path.abspath(__file__))

class DevServer(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == '/api/save':
            self.handle_save()
        else:
            self.send_error(404, 'Not found')

    def handle_save(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body.decode('utf-8'))

            filepath = data.get('path', '')
            content = data.get('content', '')

            # Security: only allow writing to known files
            allowed = ['articles/articles.json', 'sitemap.xml', 'rss.xml']
            if filepath not in allowed:
                self.send_json(403, {'error': 'File not allowed: ' + filepath})
                return

            full_path = os.path.join(ROOT, filepath.replace('/', os.sep))
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)

            self.send_json(200, {'success': True, 'path': filepath})
            print(f'  [SAVED] {filepath} ({len(content)} bytes)')

        except Exception as e:
            self.send_json(500, {'error': str(e)})

    def send_json(self, code, obj):
        body = json.dumps(obj).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(body))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    print(f'Dev server running at http://localhost:{PORT}')
    print(f'Dashboard: http://localhost:{PORT}/articles/dashboard.html')
    print(f'Press Ctrl+C to stop')
    http.server.HTTPServer(('0.0.0.0', PORT), DevServer).serve_forever()
