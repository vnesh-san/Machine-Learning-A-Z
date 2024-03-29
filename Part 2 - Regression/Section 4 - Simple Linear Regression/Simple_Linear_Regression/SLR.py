# -*- coding: utf-8 -*-
"""
Created on Sun May 13 09:47:20 2018

@author: vikuv
"""

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

#fitting SLR to dataset
from sklearn.linear_model import LinearRegression
mdl = LinearRegression()
mdl.fit(X_train, y_train)
pred = mdl.predict(X_test)
acc = mdl.score(X_test,y_test)

#plot
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, mdl.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

 