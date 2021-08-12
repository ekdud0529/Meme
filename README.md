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
>> **KcBERT**
>>> 네이버 뉴스에서 대댓글을 수집해 tokenizer와 BERT 모델을 처음부터 학습한 Pretrained 모델
>>> 구어체ㅘ 신조어, 오탈자 등의 표현에 좀 더 유용하다고 판단해 사용함
>>> EX.
>>> <div><img width="700" src="https://user-images.githubusercontent.com/45174177/129136239-57d5fc3f-480e-45d9-b9a5-13845c49312f.png"></div>

### 3. Indexing
> BERT를 수행하는데는 상당한 시간이 걸리므로, 이를 통해서만 해당 프로젝트를 구현하기에는 무리가 있다고 판단했다. 시간 단축을 위해서 Faiss라는 Facebook AI Research에 의해 개발된 라이브러리를 이용하였다.
>> **Faiss**
>>> 대용량 데이터의 효율적인 유사성 검색 및 클러스터링을 위한 라이브러리
>>> 임베딩된 태그 데이터들을 인덱싱해둔다면, 검색어와 유사한 결과값을 비교 반환하는 시간을 단축 가능
>>> 때문에 Faiss를 이용해 태그 데이터들을 인덱싱 해두었고, 가장 유사한 결과값을 비교 반환하였다.

### 4. 카카오톡 연결
> 시간 관계상 가장 접근하기 좋은 플랫폼이라고 판단해 카카오톡 플러스 친구로 서비스를 제공했다.
> 카카오 i 오픈빌더에서 사용자에게 받아오는 발화 패턴이 일정하지 않기 때문에 폴백 블록을 이용했다.
> 폴백 블록에서는 스킬 데이터를 사용하여 봇 시스템으로부터 스킬 요청을 받고 이에 담긴 정보를 분석하여 적절한 응답을 만든다. 각 요청은 HTTP POST를 통해 전달되고, 요청과 응답 모두 JSON으로 구성된 body를 이용한다.

### 5. AWS EC2
> 해당 카카오톡을 백그라운드로 실행시키기 위한 서버로 AWS EC2를 사용했다.

## Test & Review
### 1. 기본 기능 - 검색
<div>
  <img width="300" height="650" src="https://user-images.githubusercontent.com/45174177/129136937-3b312a3f-b4e7-4c5c-8f46-7df72fb1e256.png">
  <img width="300" height="650" src="https://user-images.githubusercontent.com/45174177/129136941-c1dc13db-f2cd-43ca-adf8-4a320973a486.png">
</div>
