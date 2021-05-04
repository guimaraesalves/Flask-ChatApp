from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World! Testando o Hank aqui."

if __name__ == "__main__":
    app.run(debug=True)
