# Meme(美味, 짤 맛집) - 밈 검색기
- 자연어 질의를 통한 밈 검색기
- 자연어 질의를 입력하면 (ex. 무야호) 자연어처리를 통해 관련된 이미지를 반환하는 시스템
- 사용자에 질의에 대해 주어진 문단에서 원하는 정답을 찾는 시스템 구현
---

## Meme
- 인터넷에서 문화요소로 유행하는 모든 것을 말할 때 사용되는 단어
- SNS 등에서 유행하여 다양한 모습으로 복제되는 짤방 혹은 패러디물

## 시스템 흐름도
<div><img width="800" src="https://user-images.githubusercontent.com/45174177/129135592-1894cc04-f063-4938-b676-356be44720bd.png"></div>

## Project
#### 1. Crawling
- 선정한 사이트(https://2runzzal.com/) 에서 크롤링을 통해 이미지 수집
- python - selenium 통해 수집후 .csv로 저장

#### 2. Embedding
자연어를 컴퓨터가 이해하고, 효율적으로 처리하게 하기 위해 컴퓨터가 이해할 수 있도록 자연어를 vector로 바꾸는 결과 혹은 일련의 과정이다.
##### **KcBERT**
- 네이버 뉴스에서 대댓글을 수집해 tokenizer와 BERT 모델을 처음부터 학습한 Pretrained 모델
- 구어체ㅘ 신조어, 오탈자 등의 표현에 좀 더 유용하다고 판단해 사용함
> EX.
> <div><img width="500" src="https://user-images.githubusercontent.com/45174177/129136239-57d5fc3f-480e-45d9-b9a5-13845c49312f.png"></div>

#### 3. Indexing
BERT를 수행하는데는 상당한 시간이 걸리므로, 이를 통해서만 해당 프로젝트를 구현하기에는 무리가 있다고 판단했다. 시간 단축을 위해서 Faiss라는 Facebook AI Research에 의해 개발된 라이브러리를 이용하였다.
##### **Faiss**
> 대용량 데이터의 효율적인 유사성 검색 및 클러스터링을 위한 라이브러리  
> 임베딩된 태그 데이터들을 인덱싱해둔다면, 검색어와 유사한 결과값을 비교 반환하는 시간을 단축 가능
> 때문에 Faiss를 이용해 태그 데이터들을 인덱싱 해두었고, 가장 유사한 결과값을 비교 반환하였다.

#### 4. 카카오톡 연결
- 시간 관계상 가장 접근하기 좋은 플랫폼이라고 판단해 카카오톡 플러스 친구로 서비스를 제공했다.
- 카카오 i 오픈빌더에서 사용자에게 받아오는 발화 패턴이 일정하지 않기 때문에 폴백 블록을 이용했다.
- 폴백 블록에서는 스킬 데이터를 사용하여 봇 시스템으로부터 스킬 요청을 받고 이에 담긴 정보를 분석하여 적절한 응답을 만든다. 각 요청은 HTTP POST를 통해 전달되고, 요청과 응답 모두 JSON으로 구성된 body를 이용한다.

#### 5. AWS EC2
해당 카카오톡을 백그라운드로 실행시키기 위한 서버로 AWS EC2를 사용했다.

## Test & Review
#### 1. 기본 기능 - 검색
<div>
  <img width="400" height="700" src="https://user-images.githubusercontent.com/45174177/129136937-3b312a3f-b4e7-4c5c-8f46-7df72fb1e256.png">
  <img width="400" height="700" src="https://user-images.githubusercontent.com/45174177/129136941-c1dc13db-f2cd-43ca-adf8-4a320973a486.png">
</div>

#### 2. 유사 의미 & 중의적 단어 구별 여부
<div>
  <img width="400" height="700" src="https://user-images.githubusercontent.com/45174177/129137229-5e45f8c5-308c-4393-9629-26804cc2f400.png">
  <img width="400" height="700" src="https://user-images.githubusercontent.com/45174177/129137236-068ad9a2-d05b-48a2-b97d-65a8cb10b152.png">
</div>

#### 3. 사용성
*사용자 16명이 이틀간 사용한 후 설문조사 진행*

##### **접근성과 사용 만족도**
<div><img width="400" src="https://user-images.githubusercontent.com/45174177/129137770-2bda6358-3f13-4082-82d2-63668d3de588.png"><img width="400" src="https://user-images.githubusercontent.com/45174177/129137775-777b6525-4a31-4efd-b07d-77cbec95d67d.png"></div>

##### **불편한 점**
- 느리다.
- 반환이 안 될 때가 있다.
- 정확도가 다소 부진하다.
- 이미지가 깨져서 전송되는 경우가 있다.

##### **총평**
- 정확도가 다소 부족하나 미묘하게 어울리는 밈이 나오는 경우가 있어서 재밌다.
- 다양한 이미지 중 선택할 수 있으면 좋겠다.
- 신선하다
- 상황에 맞는 사진을 찾는 것이 번거로웠는데, 한결 편한 것 같다.
- 짤을 수집할 때 굉장히 유용하다.

## 기대효과 및 활용방안
1. 사용자는 검색 후 이미지를 판별하고 선택하는 시간이 단축되고, 이미지의 활용도가 향상될 것이다.
2. 현재 카카오톡과 라인에서는 아래 사진과 같이 채팅창에 입력 중인 글과 관련된 이모티콘을 추천해 주는 서비스를 제공하는 중이다. 이러한 기능을 블로그나 카페, 뉴스 등 댓글을 작성할 수 있는 플랫폼에 같은 방식으로 적용 방향을 확대할 수 있다.
<div>
  <img width="400" height="400" src="https://user-images.githubusercontent.com/45174177/129138540-3cbc0dd9-2882-4c37-817f-ed9de6919ecd.png">
</div>

## 개선 방향
1. 서버 개선
2. KcBERT를 주어진 데이터로 사전학습을 시켜 사용
3. .webp 이미지는 깨져서 나오기 때문에 jpg, png, gif 파일로 변환해서 사용하기
4. 이미지 여러개 반환 가능하게 하기


## 참고 자료
- 크롤링
  + https://www.youtube.com/watch?v=1b7pXC1-IbE&t=1735s

- BERT
  + https://github.com/Beomi/KcBERT
  + https://ratsgo.github.io/nlpbook/docs/language_model/tutorial/
  + https://pytorch.org/
  + https://github.com/huggingface/transformers#installation
  
- Faiss
  + https://github.com/facebookresearch/faiss
  + https://lsjsj92.tistory.com/605

- 카카오 i 오픈빌더
  + https://i.kakao.com/docs/getting-started-overview#%EC%98%A4%ED%94%88%EB%B9%8C%EB%8D%94-%EC%86%8C%EA%B0%9C
