from flask import Flask

app = Flask(__name__)

@app.route("/") # decorator
def home(): # route handler function
    # returning a response
    return "Hello World"

app.run()