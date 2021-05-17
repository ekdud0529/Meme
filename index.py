from flask import Flask, request, jsonify
import data2vec

ERROR_MESSAGE = '네트워크 접속에 문제가 발생하였습니다. 잠시 후 다시 시도해 주세요.'

app = Flask(__name__)

# 서버 작동 확인
@app.route("/")
def hello():
    return "Hello, Flask!"

# https://meme-uerun.run.goorm.io/
@app.route('/meme', methods=['POST'])
def memeSearch():
    req = request.get_json()

    req = req['userRequest']['utterance']

    # 검색어 임베딩
    answer = data2vec.tagEmbedding(req)
    answer = data2vec.search_meme(answer)
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer
                    }
                }
            ]
        }
    }

    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)