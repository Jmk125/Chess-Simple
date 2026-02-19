#!/usr/bin/env python3
"""Serve Chess-Simple with headers needed for SharedArrayBuffer-based Stockfish builds."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import argparse


class COIHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cross-Origin-Resource-Policy", "cross-origin")
        super().end_headers()


def main():
    parser = argparse.ArgumentParser(description="Serve files with COOP/COEP headers for Stockfish threaded builds.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=4173)
    args = parser.parse_args()

    server = ThreadingHTTPServer((args.host, args.port), COIHandler)
    print(f"Serving with COOP/COEP on http://{args.host}:{args.port}/")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")


if __name__ == "__main__":
    main()
