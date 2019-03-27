# Session
# Session 是每个 Tensorflow 文件都需要的步骤.
# 运行 seesion.run()可以获得你要得知的运算结果

import tensorflow as tf

matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],
                       [2]])

product = tf.matmul(matrix1, matrix2)  #martrix multiply

# method 1
sess = tf.Session()
result = sess.run(product)
print(result)  #result = [[12]]
sess.close()


# method 2
with tf.Session() as sess:    #不需要sess.close()
    result2 = sess.run(product)
    print(result2)
