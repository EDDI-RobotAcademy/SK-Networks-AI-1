from typing import List

from pydantic import BaseModel
import tensorflow as tf



class PredictRequest(BaseModel):
    X: list

    # 리스트 형식이면 gpu 계산이 안되기 때문에 tensor로 바꿔줘야 함
    # 이미지를 바꾸는 것과 같이 우리 수준에서 처리할 수 있지만 gpu 수준에서 하기 위해서는 tensor를 써줘야함
    # list 였던 X를 tf.Tensor로 변환
    def toTensor(self):
        return tf.constant(self.X, dtype=tf.float32)

