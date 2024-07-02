import tensorflow as tf


class LinearRegressionModel(tf.Module):
    def __init__(self):
        self.weight = tf.Variable(tf.random.uniform([1], -1.0, 1.0))
        self.intercept = tf.Variable(tf.zeros([1]))

    def __call__(self, x):
        return self.weight * x + self.intercept