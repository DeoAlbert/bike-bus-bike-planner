#!/usr/bin/env python3
"""
Simple server for Railway deployment
"""
import os
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver

# Get port from Railway environment
PORT = int(os.environ.get('PORT', 8000))

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Bike-Bus-Bike Route Planner</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 40px; }
                    .container { max-width: 800px; margin: 0 auto; }
                    .header { background: #2c3e50; color: white; padding: 20px; border-radius: 5px; }
                    .content { padding: 20px; }
                    .status { background: #27ae60; color: white; padding: 10px; border-radius: 3px; margin: 10px 0; }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>🚴 Bike-Bus-Bike Route Planner</h1>
                        <p>Multimodal Transportation Route Planning</p>
                    </div>
                    <div class="content">
                        <div class="status">
                            ✅ Server is running successfully!
                        </div>
                        <h2>Features:</h2>
                        <ul>
                            <li>🚴 Google Maps bicycle routing</li>
                            <li>🚌 Real-time transit data</li>
                            <li>🛡️ Safety scoring for bike routes</li>
                            <li>🔄 Smart multimodal planning</li>
                        </ul>
                        <p><strong>Status:</strong> Application deployed and ready!</p>
                        <p><strong>Port:</strong> {}</p>
                    </div>
                </div>
            </body>
            </html>
            """.format(PORT)
            
            self.wfile.write(html.encode())
            
        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            health = {
                "status": "healthy",
                "service": "Bike-Bus-Bike Route Planner",
                "port": PORT
            }
            self.wfile.write(json.dumps(health).encode())
            
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    print(f"Starting simple server on port {PORT}")
    print(f"Environment PORT: {os.environ.get('PORT', 'not set')}")
    
    try:
        with socketserver.TCPServer(("0.0.0.0", PORT), SimpleHandler) as httpd:
            print(f"Server running at http://0.0.0.0:{PORT}")
            print("Press Ctrl+C to stop")
            httpd.serve_forever()
    except Exception as e:
        print(f"Error starting server: {e}")
        exit(1)
