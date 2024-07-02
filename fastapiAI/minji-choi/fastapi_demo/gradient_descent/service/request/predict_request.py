from typing import List
import tensorflow as tf
from pydantic import BaseModel

class PredictRequest(BaseModel):
    X : list
    def toTensor(self):
        return tf.constant(self.X, dtype=tf.float32)


