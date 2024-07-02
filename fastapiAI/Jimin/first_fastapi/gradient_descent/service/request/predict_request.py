from pydantic import BaseModel
import tensorflow as tf


class PredictRequest(BaseModel):
    X: list
    # tensor는 행렬이 큐브형태를 이루고 있다고 생각
    # 스칼라, 벡터의 상위 개념

    def toTensor(self):
        # 자료형을 tensor로 바꾸고 싶을때 constant를 사용한다.
        # list였던 X를 tf.Tensor로 변환
        # postman에서 내가 적었던 X 값이 이 X이다.
        return tf.constant(self.X, dtype=tf.float32)
