from typing import List

from pydantic import BaseModel

import tensorflow as tf


class PredictRequest(BaseModel):
    X: list

    def __init__(self, X):
        self.X = X

    def convertListToTensor(self):
        return tf.constant(self.X, dtype=tf.float32)