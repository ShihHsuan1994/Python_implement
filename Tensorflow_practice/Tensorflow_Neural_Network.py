# 在tensorflow 中定義一個添加層
# Weights, biases 為神經層中常見的參數

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


# 定義神經層函數 add_layer(), 他有四個參數: input, input大小, output大小, 激勵函數 
def add_layer(inputs, in_size, out_size, activation_function=None): #預設激勵函數為None

    # 定義Weights biases
    # Weights 是一個隨機的 [in_size,out_size] Variable矩陣
    # biases 類似一個列表 不是矩陣  推薦盡量不為0 所以 +0.1
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)  #一行多列

    # 定義 Wx_plus_b 為神經網絡未激活的值
    Wx_plus_b = tf.matmul(inputs, Weights) + biases  # matmul 為矩陣的乘法
    if activation_function is None: 
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


##########

# 建構數據 並多加noise 看起來更像真實情況
x_data = np.linspace(-1,1,300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape).astype(np.float32)
y_data = np.square(x_data) - 0.5 + noise

# 利用 tf.placeholder() 定義所需神經網絡的輸入
xs = tf.placeholder(tf.float32, [None, 1]) # None 代表輸入多少都可以，
ys = tf.placeholder(tf.float32, [None, 1]) # 因為只有輸入一個特徵所以是 1


# 建立網絡

# 建構 輸入層1個 隱藏層10個 輸出層1個 的神經網絡

# 定義隱藏層 利用add_layer()  這邊使用tensorflow自帶的激勵函數 tf.nn.relu
# 輸入xs 1個神經元  輸出10個
layer1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)

# 定義輸出層  此時輸入為 隱藏層的輸出- layer 輸入10層 輸出1層
# 輸入layer1 10個神經元  輸出1個
prediction = add_layer(layer1, 10, 1, activation_function=None)

# 計算和真實值的誤差 平方差的和 再取 平均 
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
                     reduction_indices=[1]))

# 用GradientDescent 來提高準確率  學習效率<1
# 以0.1的效率來最小化誤差loss
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss) 

# 使用 variable 時，都要進行初始化
init = tf.global_variables_initializer()

# 定義 Session  用Session 來執行 init
sess = tf.Session()
sess.run(init)

# 將data畫出來
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
plt.ion()  #連續顯示
plt.show()

# Training
# 當運算要用 placeholder 時，就需要 feed_dict 來指定輸入
for i in range(1000):
    sess.run(train_step, feed_dict={xs:x_data, ys: y_data})
    if i % 50 == 0:   # 每50步 輸出 學習誤差
        print(sess.run(loss,feed_dict={xs:x_data, ys:y_data}))

        # 視覺化結果
        try:    #每次都要先remove line[0]的線
            ax.lines.remove(lines[0])  #先remove  再plot
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs:x_data}) #輸出prediction的值
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5) #曲線方式 以紅色 寬度5的線表示
        plt.pause(0.1)  #每次暫停0.1sec


