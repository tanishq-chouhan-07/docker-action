from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import redis
import json

cache = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    decode_responses=True,
    socket_connect_timeout=2
)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            visits = cache.incr("visits")
            result = {
                "message": "Hello from Compose!",
                "visits": visits
            }
            status = 200
        except redis.RedisError:
            result = {"error": "Redis is unavailable"}
            status = 503

        body = json.dumps(result).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
