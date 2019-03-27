# Placeholder
# Tensorflow 如果想要从外部传入data 時使用

import tensorflow as tf

input1 = tf.placeholder(tf.float32)   #placeholder 要給他一個typ 通常是float32
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1, input2)  #multiply 是將input1 2 做相乘

with tf.Session() as sess:  #需要傳入的值放在 feed_dict={}
    print(sess.run(output, feed_dict={input1:[7.], input2:[2.]}))
