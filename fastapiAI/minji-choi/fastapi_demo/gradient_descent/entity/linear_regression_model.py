import tensorflow as tf

class LinearRegressionModel(tf.Module):
    def __init__(self):
        self.weight = tf.Variable(tf.random.uniform([1], -1.0, 1.0, dtype=tf.float32))
        self.intercept = tf.Variable(tf.zeros([1], dtype=tf.float32)) # 절편

    def __call__(self, x):
        return self.weight * x + self.intercept