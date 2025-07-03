from flask import Flask
import argparse

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Example api starting")
    parser.add_argument('--port', type=int, default=8080, help='Api port')
    parser.add_argument('--host', type=str, default='localhost', help='Api host')
    args = parser.parse_args()
    app.run(host=args.host, port=args.port)
