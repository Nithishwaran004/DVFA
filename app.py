from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "suchSecret"

from routes import *

if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5000)
