from pydantic import BaseModel

import tensorflow as tf


class PredictRequest(BaseModel):
    X: list

    def toTensor(self):
        # list를 tensor로 만들려면 tf.constant를 써라
        return tf.constant(self.X, dtype=tf.float32)