# Layerd Architecture를 구성할 때

```commandLine
아래의 4가지를 구성하게 됩니다.
entity, controller, service, repository
```

## 각각의 역할은 무엇인가?


### entity(핵심 업무 규칙)
```commandline
보편적으로 entity는 특정 주제를 표현하는 핵심 정보에 해당합니다.
사용자 정보를 다루는 주제에서는 사용자 정보 자체가 entity에 해당합니다.
상품 정보를 다루는 경우엔 상품 정보 자체가 entity가 됩니다.
```

### comtoroller(외부 요청 처리)

```commandline
서버와 클라이언트가 있을 때
클라이언트의 요청을 수신하고 적절하게 처리하기 위해 존재합니다.
```

### service(중간 레이어)
```commandline
엄밀하게 중간 레이어라고 할 수 없지만 조반이니 이렇게 생각라자
가장 좋은 예라면 Orde(주문) 상황입니다.
Product(상품)과 Account(회원) 정보가 있을 때
주문은 Product와 Account정보가 모두 필요합니다.

효율적인 코드를 작성한다고 가정한다면
아래와 같은 표현을 할 수 있겠습니다.
Order Service에서 Product Repository와 Account Repository를 재활용합니다.


이와 같은 상황을 구성하기 위한 목적으로써도
service 레이어는 중요한 역할을 가지고 있습니다.

현재 우리가 만든 Dice케이스는 service Layer의 의미가 모호한 상태입니다.
```


### repository (실직적인 데이터 처리 혹은 기술적인 요소 처리)

```commandline
repository는 실제 전문 개발자들이 직접 제어해야 하는 요소둘울 배치하거나
특정 domain 특화 지식들을 직접적으로 다루는 상황
혹은 DB에 데이터를 직접 입력하는 상홛 등의 케이르를 다룹니다.
```