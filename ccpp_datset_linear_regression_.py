# -*- coding: utf-8 -*-
"""CCPP DATSET LINEAR REGRESSION .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J_yWTXWFJqm2WHwO4gYOE0w4rXytDH09

NAME:BHAVYATHA.B
ROLL NUMBER: 20191ISE0026
# LINEAR REGRESSION MINI PROJECT

# Import Libraries
"""

import pandas as pd
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

f=open('/content/drive/MyDrive/PSP/Folds5x2_pp.xlsx - Sheet1.csv','r')

content=f.read()
print(content)

f.close()

"""# Import dataset"""

data_df=pd.read_csv("/content/drive/MyDrive/PSP/Folds5x2_pp.xlsx - Sheet1.csv")

data_df.head()

"""# Define x and y """

x=data_df.drop(['PE'],axis=1).values
y=data_df['PE'].values

print(x)

print(y)

"""## Split the dataset in training set and test set """

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

"""# Train the model on the traning set bold text"""

from sklearn.linear_model import LinearRegression
ml=LinearRegression()
ml.fit(x_train,y_train)

"""# Predict the test set results """

y_pred=ml.predict(x_test)
print(y_pred)

ml.predict([[14.96,41.76,1024.07,73.17]])

"""# Evaluate the model"""

from sklearn .metrics import r2_score
r2_score(y_test,y_pred)

"""# Plot the results"""

import matplotlib.pyplot as plt
plt.figure(figsize=(15,10))
plt.scatter(y_test,y_pred)
plt.xlabel('Actual')
plt.ylabel('Actual vs. Predicted')

"""Predicted values"""

pred_y_df=pd.DataFrame({'Actual Value':y_test,'Predicted value':y_pred,'Difference': y_test-y_pred}) 
pred_y_df[0:20]