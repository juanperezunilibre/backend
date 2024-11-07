from flask import Flask, request
import json
import bcrypt

app = Flask(__name__)

@app.get("/products")
def index():
    with open("data.json", "r") as file:
        products = json.load(file)
    return products

@app.post("/product")
def create_product():
    data = json.loads(request.data)
    with open("data.json", "w") as file:
        json.dump(data, file)

    return {
        "status": "success",
        "message": "Product added successfully"
    }

@app.get("/encrypt/<password>")
def encrypt(password: str):
    print(password)
    
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


if __name__ == '__main__':
    app.run(debug=True)



