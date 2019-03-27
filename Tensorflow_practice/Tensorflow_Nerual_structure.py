#

import tensorflow as tf
import numpy as np


#create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3   #x希望接近0.1  y希望接近0.3

### create tensorflow structure 搭建模型
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data)) #計算誤差

#反向傳遞誤差，使用 Gradient Descent 方法
optimizer = tf.train.GradientDescentOptimizer(0.5)  #學習效率<1
train = optimizer.minimize(loss)

#Train
init = tf.global_variables_initializer()

### create tensorflow structure

#用session初始化，並 run 每次 training 數據
sess = tf.Session()
sess.run(init)    #激活init


for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))
