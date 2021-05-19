from flask import Flask, request, jsonify
import time

ERROR_MESSAGE = '네트워크 접속에 문제가 발생하였습니다. 잠시 후 다시 시도해 주세요.'

app = Flask(__name__)

# 서버 작동 확인
@app.route("/")
def hello():
    return "Hello, Flask!"

# 토크나이저 초기화
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained(
    "beomi/kcbert-base",
    do_lower_case=False,
)
#모델 초기화
from transformers import BertConfig, BertModel
pretrained_model_config = BertConfig.from_pretrained(
    "beomi/kcbert-base"
)

# KcBERT embedding
import torch
model = BertModel.from_pretrained(
    "beomi/kcbert-base",
    config=pretrained_model_config,
)

def searchWordEmbedding(searchWord):

    features = tokenizer(
        searchWord,
        max_length=40,
        padding="max_length",
        truncation=True,
    )

    features = {k: torch.tensor(v) for k, v in features.items()}
    outputs = model(**features)

    return outputs

# faiss indexing read
import faiss
index2 = faiss.read_index("memeTag.index")

def search_meme(search):

    search_outputs = search

    # 검색어 비교 및 반환
    searchVec = search_outputs[1].detach().numpy()
    distances, indices = index2.search(searchVec, 3)
    return indices

# https://meme-uerun.run.goorm.io/
@app.route('/meme', methods=['POST'])
def memeSearch():
    req = request.get_json()

    req = req['userRequest']['utterance']

    req = req.split()

    # 검색어 임베딩
    answer = searchWordEmbedding(req)
    answer = search_meme(answer)
    answer = " ".join(map(str, answer))
    print(answer)

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