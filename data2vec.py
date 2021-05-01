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

# 임의로 설정한 검색어
search = ['이쁘다', '짱구']

#검색어 KcBERT로 imbedding
search_features = tokenizer(
    search,
    max_length=40,
    padding="max_length",
    truncation=True,
)

search_features = {k: torch.tensor(v) for k, v in search_features.items()}

search_outputs = model(**search_features)

print(search_outputs[1])

# 검색어 비교 및 반환