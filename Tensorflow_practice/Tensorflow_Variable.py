# Variable

import tensorflow as tf

state = tf.Variable(0, name='counter')

#定義 one
one = tf.constant(1) 

#定義加法步驟
new_value = tf.add(state, one)

#將 state 更新為 new_value
update = tf.assign(state, new_value)

init = tf.initialize_all_variables() #如果有定義variable一定要此行

#使用Session
with tf.Session() as sess:
    sess.run(init)
    for _ in range(4):
        sess.run(update)
        print(sess.run(state))
