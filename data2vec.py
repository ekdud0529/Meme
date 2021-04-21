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

sentences = ["무라세사에, 졸이쁨, 인기", "지켜본다, 으으으, 끔찍", "생각", "짱구", "?!", "양파", "제니", "양파죠", "불꽃놀이", "오마이걸", "엠넷", "엠카", "엠카운트다운", "갓세븐, 럴러바이, M COUNTDOWN"]
features = tokenizer(
    sentences,
    max_length=40,
    padding="max_length",
    truncation=True,
)

features = {k: torch.tensor(v) for k, v in features.items()}

outputs = model(**features)

print(outputs[1])