from flask import Flask
import platform

app = Flask(__name__)

@app.route('/')
def hello():
    arch = platform.machine()
    return f"Hello from {arch} architecture!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)