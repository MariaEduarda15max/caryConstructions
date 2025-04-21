from flask import Flask

 = Flask(__name__)

@app.route("/")
def home():
    return "Hola desde Flask en iPhone!"

if __name__ == "__main__":
    app.run(host="-2.0.0.0", port=799c
            )
