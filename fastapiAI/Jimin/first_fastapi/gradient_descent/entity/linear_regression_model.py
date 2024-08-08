import tensorflow as tf

class LinearRegressionModel(tf.Module):
    def __init__(self):
        # tf.Variable: 예네들을 학습시켜서 최적의 값으로 계속 업데이트 시키겠다.
        self.weight = tf.Variable(tf.random.uniform([1], -1.0, 1.0))
        self.intercept = tf.Variable(tf.zeros([1]))

    def __call__(self, x):
        return self.weight * x + self.intercept
    # y = wX + b >> w,b가 최종적인 y에 가까워지도록 학습