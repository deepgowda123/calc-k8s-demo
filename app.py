from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Calculator API (K8s demo)!"

@app.route("/health")
def health():
    return "OK", 200

def get_ab():
    a = request.args.get("a", type=float, default=0)
    b = request.args.get("b", type=float, default=0)
    return a, b

@app.route("/add")
def add():
    a, b = get_ab()
    return jsonify(result=a + b)

@app.route("/sub")
def sub():
    a, b = get_ab()
    return jsonify(result=a - b)

@app.route("/mul")
def mul():
    a, b = get_ab()
    return jsonify(result=a * b)

@app.route("/div")
def div():
    a, b = get_ab()
    if b == 0:
        return jsonify(error="Division by zero not allowed"), 400
    return jsonify(result=a / b)

if __name__ == "__main__":
    # listen on all interfaces for Docker/K8s, port 5000
    app.run(host="0.0.0.0", port=5000)
