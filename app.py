from flask import Flask

app = Flask(__name__)

@app.route('/')
def hi():
    return 'Hello World!'

@app.route('/wel')
def welcome():
    return 'Welcome to The Game!'

if __name__ == '__main__':
    app.run()

