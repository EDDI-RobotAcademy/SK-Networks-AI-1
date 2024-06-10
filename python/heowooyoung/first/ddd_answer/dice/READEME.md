### Layered Architecture를 구성 할때

```commandline
아래의 4가지를 구성하게 됩니다.
entitiy, controller, service, repository
```

### 각각의 역할은 무엇인가?

### entity (핵심 업무 규칙)

```commandline
보편적으로는 entity는 특정 주제를 표현하는 핵심 정보에 해당합니다.
사용자 정보를 다루는 주제에는 사용자 정보 자체가 entity에 해당합니다.
상품 정보를 다루는 경우엔 상품 정보 자체가 entitiy가 됩니다.
```

### controller (외부 요청 처리)

```commandline
서버와 클라이언트가 있을 때 클라이어트의 요청을 수신하고 적절하게 처리하기 위해 존재합니다.
서버는 업주 클라이언트는 고객이라고 생각하고 이해하면 편하다.
```

### service (중간 레이어)
```commandline
엄밀하게 중간 레이러라고 할 수 없지만 초반이니 이렇게 생각하자
가장 좋은 예라면 Order(주만) 상황입니다.
Product(상품)과 Account(회원) 정보가 있을 때
주문은 Product와 Account 정보가 모두 필요합니다.

효율적인 코드를 작성한다고 가정하면
아래와 같은 표현을 할 수 있을 것입니다.
Order Service에서 Product Repository와 Account Repository를 재활용합니다.
service 레이어는 중요한 열할을 가지고 있습니다.
현재 우리가 만들 Dice 케이스는 service layer의 의미가 모호한 상태입니다.
```

### repository (실직적인 데이터 처리 혹은 기술적인 요소 처리)
```commandline
repository는 실제 전문 개발자들이 직접 제어해야 하는 요소들을 배치하거나
특정 domain 특화 지식들을 직접적으로 다루는 상황
혹은 DB에 데이터를 직업 입력하는 상황 등의 케이스를 다룹니다.
```
