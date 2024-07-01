import tensorflow as tf

class LinearRegressionModel(tf.Module):

    def __init__(self):
        # super().__init__(name=name)
        self.weight = tf.Variable(tf.random.uniform([1], -1.0, 1.0), trainable=True)
        self.intercept = tf.Variable(tf.zeros([1]), trainable=True)

    def __call__(self, x):
        return self.weight * x + self.intercept # 해당 클래스를 호출한다면 회귀 식 반환