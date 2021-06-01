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

    return outputs[1]


def tagIndexing(outputs): 

    import faiss

    tagVec = outputs[1].detach().numpy() # numpy로 형변환
    index = faiss.IndexFlatL2(tagVec.shape[1])
    index.add(tagVec)
    print(index.ntotal)

    # faiss indexing save
    faiss.write_index(index, "TagIndexing.index")

import csv
def readTag():
    data = []
    # encoding='utf-8-sig' 설정은 한글 깨짐 방지
    f = open('imgData.csv', 'r', encoding='utf-8-sig')
    rdr = csv.reader(f)
    for line in rdr:
        data.append(line)
    f.close

    return data

def list2csv(crawlingList) :
    # newline='' 설정이 없는 경우 row와 row 사이에 뉴라인이 한번 더 들어가게 됨
    f = open('tagE1.csv', 'w', newline='')
    wr = csv.writer(f)
    for imgList in crawlingList:
        wr.writerow(imgList)
    f.close()

# tagData = readTag()
# vec1 = tagData[: 1001]
# vec2 = tagData[1000:2001]
# vec3 = tagData[2001:3001]
# vec4 = tagData[3001:4001]
# vec5 = tagData[4001:5001]
# vec6 = tagData[5001:6001]
# vec7 = tagData[6001:]


# out1 = tagEmbedding(vec1)
# out2 = tagEmbedding(vec2)
# out3 = tagEmbedding(vec3)
# out4 = tagEmbedding(vec4)
# out5 = tagEmbedding(vec5)
# out6 = tagEmbedding(vec6)
# out7 = tagEmbedding(vec7)

# outnp = out7.detach().numpy()

import numpy as np
# np.save('C:/Users/ekffk/tagFile/tag7', outnp)
out1_load = np.load('C:/Users/ekffk/tagFile/tag1.npy', allow_pickle=True)
out2_load = np.load('C:/Users/ekffk/tagFile/tag2.npy', allow_pickle=True)
out3_load = np.load('C:/Users/ekffk/tagFile/tag3.npy', allow_pickle=True)
out4_load = np.load('C:/Users/ekffk/tagFile/tag4.npy', allow_pickle=True)
out5_load = np.load('C:/Users/ekffk/tagFile/tag5.npy', allow_pickle=True)
out6_load = np.load('C:/Users/ekffk/tagFile/tag6.npy', allow_pickle=True)
out7_load = np.load('C:/Users/ekffk/tagFile/tag7.npy', allow_pickle=True)

total_output = np.concatenate((out1_load, out2_load), axis=0)
total_output = np.concatenate((total_output, out3_load), axis=0)
total_output = np.concatenate((total_output, out4_load), axis=0)
total_output = np.concatenate((total_output, out5_load), axis=0)
total_output = np.concatenate((total_output, out6_load), axis=0)
total_output = np.concatenate((total_output, out7_load), axis=0)

print(total_output)

# tagIndexing(outputs)