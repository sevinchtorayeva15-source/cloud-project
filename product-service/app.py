from flask import Flask, jsonify

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Olma", "price": 12000},
    {"id": 2, "name": "Non", "price": 4000},
    {"id": 3, "name": "Sut", "price": 9000},
]

@app.route("/products")
def products():
    return jsonify(PRODUCTS)

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
