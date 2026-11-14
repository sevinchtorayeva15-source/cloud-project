import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

PRODUCT_URL = os.getenv("PRODUCT_URL", "http://product-service:5001")

@app.route("/orders")
def orders():
    products = requests.get(f"{PRODUCT_URL}/products", timeout=5).json()
    result = [
        {"order_id": 100 + p["id"], "product": p["name"], "total": p["price"] * 2, "qty": 2}
        for p in products
    ]
    return jsonify(result)

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
