# KcBERT embedding
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained(
    "beomi/kcbert-base",
    do_lower_case=False,
)

from transformers import BertConfig, BertModel
pretrained_model_config = BertConfig.from_pretrained(
    "beomi/kcbert-base"
)

import torch
model = BertModel.from_pretrained(
    "beomi/kcbert-base",
    config=pretrained_model_config,
)

import csv
def csv2list() :
    data = []
    # encoding='utf-8-sig' 설정은 한글 깨짐 방지
    f = open('tagData.csv', 'r')
    rdr = csv.reader(f)
    for line in rdr:
        data.append(line)
    f.close

    return data

sentences = csv2list()
print(sentences)
print("\n\n\n\n")

features = tokenizer(
    sentences,
    max_length=40,
    padding="max_length",
    truncation=True,
)

features = {k: torch.tensor(v) for k, v in features.items()}

outputs = model(**features)

print(outputs[1])


# indexing
import faiss

tagVec = outputs[1].detach().numpy()
index = faiss.IndexFlatL2(tagVec.shape[1])
index.add(tagVec)
print(index.ntotal)

# 검색어 입력받기
#search = input()

#검색어 KcBERT로 imbedding


# 검색어 비교 및 반환