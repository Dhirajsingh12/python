from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"id": 1, "name": "Wireless Earbuds", "price": 49.99, "image": "earbuds.jpg"},
    {"id": 2, "name": "Smart Watch", "price": 79.99, "image": "smartwatch.jpg"},
    {"id": 3, "name": "Bluetooth Speaker", "price": 39.99, "image": "speaker.jpg"},
]

@app.route("/")
def index():
    return render_template("index.html", products=products)

@app.route("/product/<int:product_id>")
def product(product_id):
    prod = next((item for item in products if item["id"] == product_id), None)
    if prod:
        return render_template("product.html", product=prod)
    return "Product not found", 404

if __name__ == "__main__":
    app.run(debug=True)
