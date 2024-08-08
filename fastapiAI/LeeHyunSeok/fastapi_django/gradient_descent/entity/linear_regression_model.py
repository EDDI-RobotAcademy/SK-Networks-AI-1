import tensorflow as tf


class LinearRegressionModel(tf.Module):
    def __init__(self):
        # tf.variable : 얘네들을 학습시켜서 최적의 값으로 계속 업데이트 시키겠다.   -> 참고로 이게 torch에서는 nn.parameter
        self.weight = tf.Variable(tf.random.uniform([1], -1.0, 1.0))
        self.intercept = tf.Variable(tf.zeros([1]))

    def __call__(self, x):
        # y = wX + b -> w,b가 최종적인 y에 가까워지도록 학습
        return self.weight * x + self.intercept     # 해당 클래스를 호출하면 회귀식으로 반환함