# guiltygear-strive-frame-data-back


## TIL
#### 2021-10-08
- 개발환경 세팅을 하였음 서버는 GCP, CI는 github Action, CD는 GCP Cloud Build를 사용하기로 하였다.
  둘다 처음 활용해 보는 기술이라 좀 해멨지만, GCP VM같은경우에는, 굉장히 시작하지 편하게 되어있었고, 
  service user를 생성해서 IAM을 제공하는게 AWS와는 다르게 직관적으로 되어있어서 서버환경은 금방 만들었다.
  CI의 경우에는 github action도 기존에 사용해봤던 Travis CI나 AWS CodePipeline과 같이 yaml 에서 동작설정을 하기때문에 크게 어려운 점은 없었다.
  다음은 GCP CloudBuild로 CD 환경을 만드 예정이다.
