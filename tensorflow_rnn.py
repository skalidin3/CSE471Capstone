import tensorflow as tf
x = tf.placeholder(tf.float32,[None,140004])
y = tf.placeholder(tf.float32,[None,8])



#We will declare (n-1) weights and biases here where n is the number of layers

W1 = tf.Variable(tf.random_normal([140004,40000], stddev=0.03), name='W1')
b1 = tf.Variable(tf.random_normal([40000]), name='b1')

W2 = tf.Variable(tf.random_normal([140004,40000], stddev=0.03), name='W2')
b2 = tf.Variable(tf.random_normal([40000]), name='b2')

W3 = tf.Variable(tf.random_normal([140004,40000], stddev=0.03), name='W3')
b3 = tf.Variable(tf.random_normal([40000]), name='b3')

W4 = tf.Variable(tf.random_normal([140004,40000], stddev=0.03), name='W4')
b4 = tf.Variable(tf.random_normal([40000]), name='b4')

W5 = tf.Variable(tf.random_normal([140004,40000], stddev=0.03), name='W5')
b5 = tf.Variable(tf.random_normal([40000]), name='b5')

W6 = tf.Variable(tf.random_normal([140004,40000], stddev=0.03), name='W6')
b6 = tf.Variable(tf.random_normal([40000]), name='b6')


# calculate the output of the hidden layer
hidden_out1 = tf.add(tf.matmul(x, W1), b1)
hidden_out1 = tf.nn.relu(hidden_out1)

hidden_out2 = tf.add(tf.matmul(hidden_out1, W2), b2)
hidden_out2 = tf.nn.relu(hidden_out2)

hidden_out3 = tf.add(tf.matmul(hidden_out2, W3), b3)
hidden_out3 = tf.nn.relu(hidden_out2)

hidden_out4 = tf.add(tf.matmul(hidden_out3, W4), b4)
hidden_out4 = tf.nn.relu(hidden_out3)

hidden_out5 = tf.add(tf.matmul(hidden_out4, W5), b5)
hidden_out5 = tf.nn.relu(hidden_out4)

y_ = tf.nn.softmax(tf.add(tf.matmul(hidden_out5, W6), b6))
