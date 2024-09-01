# -*- coding: utf-8 -*-
"""ML_Project_Task1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1f7fovICjDXiPtVXZzXW_Qb5N_f4gBmWl
"""



# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import f1_score
# Load training data from CSV file
train_file = '/content/drive/MyDrive/Colab Notebooks/mnist_train.csv'

# Load testing data from CSV file
test_file = '/content/drive/MyDrive/Colab Notebooks/mnist_test.csv'

training_data = np.genfromtxt(train_file, delimiter=",")
testing_data = np.genfromtxt(test_file, delimiter=",")

# Separate features  and labels  for training data
train_digit_lables = training_data[:, 0]   # labels - consider only the first coloumn
train_pixcel_features = training_data[:, 1:]  # features- consider all coloumns exept 1st one

#print("\nshape of TRAIN features")
#print(train_pixcel_features.shape)


#print(train_digit_lables)
#print(train_pixcel_features)

# Separate features (X) and labels (y) for testing data
test_digit_lables = testing_data[:, 0]  # labels - consider only the first coloumn
test_pixcel_features = testing_data[:, 1:]  # features - consider all coloumns exept 1st one

#print("\nshape of TEST features")
#print(test_pixcel_features.shape)


# Initialize Gaussian Naive Bayes classifier
gnb = GaussianNB()

# Train the model using the training sets
gnb.fit(train_pixcel_features, train_digit_lables)

# Predict the response for test dataset
prediction = gnb.predict(test_pixcel_features) #crcuical step where we check how our model is trained
#print("\nprediction is:")
#print(prediction)

conf_matrix = confusion_matrix(test_digit_lables, prediction)
print("\nConfusion Matrix:")
print(conf_matrix)

# Calculate the accuracy of the model
accuracy = accuracy_score(test_digit_lables, prediction)
print("\n THE ACCURACY IS:", accuracy)

# Calculate precision for each class
precision = precision_score(test_digit_lables, prediction, average=None)


# Print precision for each class
print("\nPrecision for each class:")
print(precision)

# Calculate precision with macro averaging
precision_macro = precision_score(test_digit_lables, prediction, average='macro')
print("\nPrecision Macro Average:", precision_macro)


# Calculate recall for each class
recall = recall_score(test_digit_lables, prediction, average=None)
# Print recall for each class
print("\nRecall for each class:")
print(recall)


# Calculate recall with macro averaging
recall_macro = recall_score(test_digit_lables, prediction, average='macro')
print("\nRecall Macro Average:", recall_macro)


# Calculate F1 score for each class
f1_scores = f1_score(test_digit_lables, prediction, average=None)
print("\nF1 Score for each class:")
print(f1_scores)

# Calculate F1 score with macro averaging
f1_macro = f1_score(test_digit_lables, prediction, average='macro')
print("\nF1 Score Macro Average:", f1_macro)