from pydantic import BaseModel
from typing import List
import tensorflow as tf
# from tensorflow.python.framework.ops import EagerTensor

class PredictRequest(BaseModel):
    X: list

    def toTensor(self):
        # list였던 X를 tf.Tensor로 변환
        return tf.constant(self.X, dtype=tf.float32)