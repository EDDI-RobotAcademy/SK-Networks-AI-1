import tensorflow as tf


class LinearRegressionModel(tf.Module):
    def __init__(self):
        # super().__init__()
        self.weight = tf.Variable(tf.random.uniform([1], -1., 1.))
        self.intercept = tf.Variable(tf.zeros([1]))

    def __call__(self, x):
        return self.weight * x + self.intercept
