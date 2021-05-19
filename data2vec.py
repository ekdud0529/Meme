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

def tagEmbedding(tagData):

    features = tokenizer(
        tagData,
        max_length=40,
        padding="max_length",
        truncation=True,
    )

    features = {k: torch.tensor(v) for k, v in features.items()}
    outputs = model(**features)
    print(outputs[1])

    return outputs



def tagIndexing(outputs): 

    import faiss

    tagVec = outputs[1].detach().numpy()
    index = faiss.IndexFlatL2(tagVec.shape[1])
    index.add(tagVec)
    print(index.ntotal)
    print("\n\n")

    # faiss indexing save
    faiss.write_index(index, "memeTag.index")

def readTag():

    import csv

    data = []
    # encoding='utf-8-sig' 설정은 한글 깨짐 방지
    f = open('memeData.csv', 'r')
    rdr = csv.reader(f)
    for line in rdr:
        data.append(line)
    f.close

    return data


