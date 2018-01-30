from __future__ import print_function
import tensorflow as tf
from tensorflow.contrib import rnn

#Training parameters
learning_rate = 0.001
training_steps = 10000
batch_size = 2
display_step = 100

#Network Parameters
num_input = 9
timesteps = 1
num_features = 128
num_classes = 8

