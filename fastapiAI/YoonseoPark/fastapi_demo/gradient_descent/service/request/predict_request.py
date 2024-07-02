from pydantic import BaseModel
import tensorflow as tf


class PredictRequest(BaseModel):
    X: list

    def toTensor(self):
        return tf.constant(self.X, dtype=tf.float32)
