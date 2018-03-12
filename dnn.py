from dnn_classifier import DNNClassifier
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

dataset = np.load('/Users/Aditya/Desktop/features.npy')
features = dataset[:,[0,1,2,3,4,5,6,7,8]]
labels = dataset[:,[9]]
X_train,X_test, y_train, y_test = train_test_split(justFeatures,labels,test_size = 0.2)
dnn = DNNClassifier(show_progress=10, random_state=42)
dnn.fit(X_train, y_train, n_epochs=100)
distraction_prediction = dnn.predict(X_test)
print("Score on test set: {:.2f}%".format(accuracy_score(y_test, distraction_predictions) * 100))

