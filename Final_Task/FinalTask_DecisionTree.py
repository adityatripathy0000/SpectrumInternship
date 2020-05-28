#Import_Library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Import_Dataset
dataset = pd.read_csv('student-math.csv', sep = ';')

#the sum of the respective three grades in the row
dataset['final_grade'] = dataset.apply(lambda row: row.G1 + row.G2 + row.G3, axis=1)

#Encode all binary values with 1 and 0 in the dataframe
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_dataset = LabelEncoder()
dataset['school'] = labelencoder_dataset.fit_transform(dataset['school'])
dataset['sex'] = labelencoder_dataset.fit_transform(dataset['sex'])
dataset['address'] = labelencoder_dataset.fit_transform(dataset['address'])
dataset['famsize'] = labelencoder_dataset.fit_transform(dataset['famsize'])
dataset['Pstatus'] = labelencoder_dataset.fit_transform(dataset['Pstatus'])
dataset['schoolsup'] = labelencoder_dataset.fit_transform(dataset['schoolsup'])
dataset['famsup'] = labelencoder_dataset.fit_transform(dataset['famsup'])
dataset['paid'] = labelencoder_dataset.fit_transform(dataset['paid'])
dataset['activities'] = labelencoder_dataset.fit_transform(dataset['activities'])
dataset['nursery'] = labelencoder_dataset.fit_transform(dataset['nursery'])
dataset['higher'] = labelencoder_dataset.fit_transform(dataset['higher'])
dataset['internet'] = labelencoder_dataset.fit_transform(dataset['internet'])
dataset['romantic'] = labelencoder_dataset.fit_transform(dataset['romantic'])

#Encode all nominal values in the dataframe
dataset['Mjob'] = labelencoder_dataset.fit_transform(dataset['Mjob'])
dataset['Fjob'] = labelencoder_dataset.fit_transform(dataset['Fjob'])
dataset['reason'] = labelencoder_dataset.fit_transform(dataset['reason'])
dataset['guardian'] = labelencoder_dataset.fit_transform(dataset['guardian'])
ct = ColumnTransformer([('encoder',OneHotEncoder(),['Mjob', 'Fjob', 'reason', 'guardian'])], remainder = 'passthrough')
dataset = np.array(ct.fit_transform(dataset), dtype = np.int64)

#Initialize X and y Variables
#X contains every column except 'G3' and 'final_grade'
X = dataset[:,:-2]
#y contains 'final_grade' column
y = dataset[:,-1]

#Splitting_Dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 0)

#Fitting_the_Model
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train, y_train)

#Predict the results
y_pred = np.int64(regressor.predict(X_test))

#Checking the score  
print('Train Score: ', regressor.score(X_train, y_train))  
print('Test Score: ', regressor.score(X_test, y_test))
print('Predict Score: ', regressor.score(X_test, y_pred))

#Visualise
plt.scatter(y_test, y_pred, color='red')
plt.title('y_pred vs y_test (Decision_Tree_Regression)')
plt.xlabel('y_test')
plt.ylabel('y_pred')
plt.show() 