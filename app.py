import os
import env
from flask import Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)

#mongo = PyMongo(app)

app.config["MONGO_DB"] = "awesome-reads"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


@app.route("/")
def base():
    return "Hello World"

if __name__ == '__main__':
            app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)