from flask import Flask, request
import json
import bcrypt
from db import db
from models.product import Product
from orm import Base, engine, Session

app = Flask(__name__)

@app.get("/products")
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products")
    products = []
    for row in cursor.fetchall():
        products.append({
            "id": row["id"],
            "name": row["name"],
            "price": row["price"]
        })
    cursor.close()
    return products

@app.post("/product")
def create_product():
    data = json.loads(request.data)

    cursor = db.cursor()
    cursor.execute("SELECT count(*) as total FROM products")

    count = cursor.fetchone()["total"]

    cursor.execute("INSERT INTO products (id, name, price) VALUES (?, ?, ?)", (count + 1, data["name"], data["price"]))
    db.commit()
    cursor.close()
    return {
        "status": "success",
        "message": "Product added successfully"
    }

@app.get("/producto/<id>")
def obtener_productos(id):
    try:
        with Session() as session:
            product = session.query(Product).where(Product.id == id).first()
        return product.to_dict()
    except Exception as e:
        return {
            "error": True,
            "message": "El producto no existe" if "None" in str(e) else str(e)
        }, 400

@app.post("/producto")
def crear_producto():
    data = json.loads(request.data)
    producto = Product(**data)
    with Session() as session:
        session.add(producto)
        session.commit()

    return {
        "status": "success",
        "message": "Product added successfully"
    }

@app.get("/encrypt/<password>")
def encrypt(password: str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=True)



