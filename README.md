# Text To Gender

## 개요

- Version : alpha(0.1)

- Url : http://www.text-to-gender.site/
- 문장을 입력해 해당 문장이 남성, 여성에 가까운 정보를 반환
- 사용 기술 스택 : Django, JavaScript, Docker
- 분류 모델 상세 : https://github.com/parkeunsang/toy_projects#community_nlp

## 웹페이지 상세

- Web, Mobile환경 지원

![image-20211012161230591](C:\Users\multicampus\projects\male_female\README.assets\image-20211012161230591.png)



- 넹 vs 네

![image-20211012161324846](C:\Users\multicampus\projects\male_female\README.assets\image-20211012161324846.png)

![image-20211012161423559](C:\Users\multicampus\projects\male_female\README.assets\image-20211012161423559.png)

## To Do List

- Classification Model : 데이터의 크기를 늘리고, 다양한 모델을 시도해 모델 고도화 필요
- Log : 사용자의 로그와 피드백 기능 등을 추가
- Deploy : 현재 django의 runserver로 서버를 구동하고있는데, nginx를 이용해 보안, 효율성 강화 필요

문의, 건의사항은 issue에 남겨주세요