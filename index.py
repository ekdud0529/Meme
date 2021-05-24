from flask import Flask, request, jsonify
from transformers import BertTokenizer
from transformers import BertConfig, BertModel
import torch
import faiss
import csv

ERROR_MESSAGE = '네트워크 접속에 문제가 발생하였습니다. 잠시 후 다시 시도해 주세요.'

app = Flask(__name__)

# 서버 작동 확인
@app.route("/")
def hello():
    return "Hello, Flask!"

# 토크나이저 초기화
tokenizer = BertTokenizer.from_pretrained(
    "beomi/kcbert-base",
    do_lower_case=False,
)

#모델 초기화
pretrained_model_config = BertConfig.from_pretrained(
    "beomi/kcbert-base"
)

# KcBERT embedding
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
tagIndex=faiss.read_index("memeTag.index")

def search_meme(search):
    search_outputs = search

    # 검색어 비교 및 반환
    searchVec = search_outputs[1].detach().numpy()
    distances, indices = tagIndex.search(searchVec, 1)
    return indices

# 이미지 가져오기
# encoding='utf-8-sig' 설정은 한글 깨짐 방지
image = []
f = open('imageData.csv', 'r')
rdr = csv.reader(f)
for line in rdr:
    image.append(line)
f.close

@app.route('/meme', methods=['POST'])
def memeSearch():
    req = request.get_json()
    req = req['userRequest']['utterance']

    # 검색어 to list
    Req = []
    Req.append(req)

    # 검색어 임베딩
    answer = searchWordEmbedding(Req)
    answer = search_meme(answer)
    print(answer)

    # 결과
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": image[0][answer[0][0]]
                    }
                }
            ]
        }
    }

    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)