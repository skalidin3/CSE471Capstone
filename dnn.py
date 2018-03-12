from dnn_classifier import DNNClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

# Reading from the features.npy file. Make sure to change the path based on the location of file on your machine
dataset = np.load('/Users/Aditya/Desktop/features.npy')

#Replacing all the '-' with 0 in order to perform computation
np.place(dataset,dataset == '-',[0])

#First 9 columns contain the feature. The last column is for the labels 
features = dataset[:,[0,1,2,3,4,5,6,7,8]]
labels = dataset[:,[9]]

#Splitting the dataset into training and testing
X_train,X_test, y_train, y_test = train_test_split(features,labels,test_size = 0.2)

#Running the DNNClassifier from the dnn_classifier file
dnn = DNNClassifier(show_progress=10, random_state=42)
dnn.fit(X_train, y_train, n_epochs=100)

#Finding the accuracy of the model
distraction_prediction = dnn.predict(X_test)
print("Score on test set: {:.2f}%".format(accuracy_score(y_test, distraction_predictions) * 100))

