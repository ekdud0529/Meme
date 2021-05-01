def search_meme() :

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

    # data 불러오기
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
    print("\n\n")

    features = tokenizer(
        sentences,
        max_length=40,
        padding="max_length",
        truncation=True,
    )

    features = {k: torch.tensor(v) for k, v in features.items()}
    outputs = model(**features)
    print(outputs[1])
    print("\n\n")


    # indexing
    import faiss

    tagVec = outputs[1].detach().numpy()
    index = faiss.IndexFlatL2(tagVec.shape[1])
    index.add(tagVec)
    print(index.ntotal)
    print("\n\n")

    # 임의로 설정한 검색어
    search1 = ['양파, 제니']
    search2 = ['짱구']

    #검색어 KcBERT로 imbedding
    search_features1 = tokenizer(
        search1,
        max_length=40,
        padding="max_length",
        truncation=True,
    )

    search_features2 = tokenizer(
        search2,
        max_length=40,
        padding="max_length",
        truncation=True,
    )

    search_features1 = {k: torch.tensor(v) for k, v in search_features1.items()}
    search_features2 = {k: torch.tensor(v) for k, v in search_features2.items()}
    search_outputs1 = model(**search_features1)
    search_outputs2 = model(**search_features1)
    print(search_outputs1[1])
    print(search_outputs2[1])
    print("\n\n")

    # 검색어 비교 및 반환
    searchVec1 = search_outputs1[1].detach().numpy()
    searchVec2 = search_outputs2[1].detach().numpy()
    distances1, indices1 = index.search(searchVec1, 1)
    distances2, indices2 = index.search(searchVec2, 1)
    print(indices1)
    print(indices2)
    print("\n\n")


search_meme()