# guiltygear-strive-frame-data-back

## TIL

#### 2021-10-08

- 개발환경 세팅을 하였음 서버는 GCP, CI는 github Action, CD는 GCP Cloud Build를 사용하기로 하였다.
  둘다 처음 활용해 보는 기술이라 좀 헤맸지만, GCP VM같은경우에는, 굉장히 시작하기 편하게 되어있었고,
  service user를 생성해서 IAM을 제공하는게 AWS와는 다르게 직관적으로 되어있어서 서버환경은 금방 만들었다.
  CI의 경우에는 github action도 기존에 사용해봤던 Travis CI나 AWS CodePipeline과 같이 yaml 에서 동작설정을 하기때문에 크게 어려운 점은 없었다.
  오히려 secret key 관리, action 정의가 깃헙 내에서 빠르게 이루어져서 너무 편했었다.
  다음은 GCP CloudBuild로 CD 환경을 만들 예정이다.

#### 2022-01-18

- 사무실 내 개발자들이 모두 퇴사하여 혼자 flutter application을 개발하느라 그동안 손대지 못했다.
  어느정도 궤도에 올랐기 때문에 다시 프로젝트를 진행해보려고 한다.
  빈 시간에 공부하면서 [django-ninja](https://django-ninja.rest-framework.com) 쪽에 흥미가 생겨 활용해보려 한다.
  routing이나 version관리가 django보다 쉬웠고 validate는 FastAPI에서 사용하던 Pydantic을 사용하기 때문에,
  django-rest-framework serializer보다 높은 성능을 기대할 수 있다.

  GCP 같은 경우엔, db설정을 잘못해서 아무 접속도 없는데 유지비만 한달에 30만원이 나오게 되었다.
  postgresql 사양을 잘못해서 높은 사양으로 잡아뒀던 것이다.
  우선 그달에 서버를 중지시켰고, 우선 docker-compose로 진행을 한 후, cloud server가 필요한 경우 다시 설정을 해주거나 AWS lambda쪽을 활용하는 방법으로 진행해야 할 것 같다.
