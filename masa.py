#import module
import os
print(os.path.abspath('.')) 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

df = pd.read_excel('MASA.xlsx')

##Train and Test Sprint (based on Commission to other variables)
#input dataframe y
y_data = df['Commision (in value)']

#drop commision data in x data
x_data=df.drop('Commision (in value)', axis=1)

#import module
from sklearn.model_selection import train_test_split

#randomly split our data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.15, random_state=1)
print("number of test samples:", x_test.shape[0])
print("number of training samples:", x_train.shape[0])

#create a Linear Regression object (for Net Sales)
x = df['Net Sales']
y = df['Commision (in value)']
import numpy as np
from sklearn.linear_model import LinearRegression
lre = LinearRegression()
lre.fit(x_train[['Net Sales']], y_train)
a = lre.score(x_test[['Net Sales']], y_test)
print(a)

lre.fit(x_test[['Net Sales']], y_test)
b = lre.score(x_train[['Net Sales']], y_train)
print(b)

#create a Linear Regression object (for Duration)
z = df['Duration']
y = df['Commision (in value)']
import numpy as np
from sklearn.linear_model import LinearRegression
lre = LinearRegression()
lre.fit(x_train[['Duration']], y_train)
c = lre.score(x_test[['Duration']], y_test)
print(c)

lre.fit(x_test[['Duration']], y_test)
d = lre.score(x_train[['Duration']], y_train)
print(d)

#create a Linear Regression object (for Age)
w = df['Age']
y = df['Commision (in value)']
import numpy as np
from sklearn.linear_model import LinearRegression
lre = LinearRegression()
lre.fit(x_train[['Age']], y_train)
e = lre.score(x_test[['Age']], y_test)
print(e)

lre.fit(x_test[['Age']], y_test)
f = lre.score(x_train[['Age']], y_train)
print(f)

###Module Development
Z = df[['Duration', 'Net Sales', 'Age']]
lre.fit(Z, df['Commision (in value)'])
print(lre.intercept_)
print(lre.coef_)

#Commision = -6.449592910116424 + 0.01586273 x Duration + 0.24843086 x Net Sales + 0.13424185 x Age

##Multiple Linear Regression
# fit the model 
lre.fit(Z, df['Commision (in value)'])

# Find the R^2
print('The R-square is: ', lre.score(Z, df['Commision (in value)']))
#We can say that ~ 43.84 % of the variation of commision is explained by this multiple linear regression

#Calculate MSE
from sklearn.metrics import mean_squared_error
Y_predict_multifit = lre.predict(Z)
print('The mean square error of commision and predicted value using multifit is: ', \
      mean_squared_error(df['Commision (in value)'], Y_predict_multifit))