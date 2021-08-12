# Meme(美味, 짤 맛집)

자연어 질의를 통한 밈 검색기
Meme search machine through natural language query
자연어 질의를 입력하면 (ex. 무야호) 자연어처리를 통해 관련된 이미지를 반환하는 시스템

---

## Meme
> 인터넷에서 문화요소로 유행하는 모든 것을 말할 때 사용되는 단어
> SNS 등에서 유행하여 다양한 모습으로 복제되는 짤방 혹은 패러디물

## Process
<div><img width="1000" src="https://user-images.githubusercontent.com/45174177/129135592-1894cc04-f063-4938-b676-356be44720bd.png"></div>

## Project
### 1. Crawling
> 선정한 사이트(https://2runzzal.com/)에서 크롤링을 통해 이미지 수집
> python - selenium 통해 수집후 .csv로 저장

### 2. Embedding
> 자연어를 컴퓨터가 이해하고, 효율적으로 처리하게 하기 위해 컴퓨터가 이해할 수 있도록 자연어를 vector로 바꾸는 결과 혹은 일련의 과정이다.
> KcBERT
>> 네이버 뉴스에서 대댓글을 수집해 tokenizer와 BERT 모델을 처음부터 학습한 Pretrained 모델
>> 구어체ㅘ 신조어, 오탈자 등의 표현에 좀 더 유용하다고 판단해 사용함

### 3. 
