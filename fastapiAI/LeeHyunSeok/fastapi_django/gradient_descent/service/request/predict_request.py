from pydantic import BaseModel
import tensorflow as tf


class PredictRequest(BaseModel):
    X:list

    def toTensor(self):
        # list였던 X를 tf.tensor로 변환
        return tf.constant(self.X, dtype=tf.float32)