# Entity

## Entity 작성 요령

1. **Entity에서는 어떠한 logic을 처리하는 코드를 작성하지 말자.**  
Entity에는 *오직 Data만 배치*하는 것이 바람직하다.
> **Dice 패키지**라면 Entity에는 **Dice**만,  
> **Player 패키지**라면 Entity에는 **Player**만 존재하도록 한다는 의미이다.
  
2. Entity에는 **get**, **set**정도만 사용하도록 한다.
> 하지만 *setter*는 가급적 지향해야 하기에,  
그 기능을 구현하는 데 *setter*가 꼭 필요한 지 고민해봐야한다.
  
3. 만약 어떤 객체가 스스로 액션(행동)을 할 수 없는 경우엔  
그 액션을 *Repository* 또는 *Service*에 구현하도록 한다.