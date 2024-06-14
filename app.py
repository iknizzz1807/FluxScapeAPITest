from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_string():
    return 'Hello nigga'

if __name__ == '__main__':
    app.run(debug=True)