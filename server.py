# API part -------------------------------------------------------------------------------------------------------------
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return "<h1>Welcome to Dodo-project Server</h1>"

@app.route("/upload", methods=['POST'])
def upload_file():
    f = request.files['...']
    f.save('./images/body.jpg')
    return 'successful'

if __name__ == '__main__':
    app.run(debug=True)
