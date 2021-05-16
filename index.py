from flask import Flask, request, jsonify

ERROR_MESSAGE = '네트워크 접속에 문제가 발생하였습니다. 잠시 후 다시 시도해 주세요.'

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)