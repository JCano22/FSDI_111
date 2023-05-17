from flask import Flask  # from the flask module import the Flask class

app = Flask(__name__)  # instantiate the Flask class into app (now an object)


@app.get("/")  # Flask decorator that maps a route to a view function
def index():  # a wrapped function is a view function in flask
    me = {
        "first_name": "Jorge",
        "last_name": "Cano",
        "hobbies": "music"
    }
    return me  # when you return a dictionary from flask view function flask will automatically convert it to JSON
