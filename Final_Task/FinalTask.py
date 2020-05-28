#Import_Library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Import_Dataset
dataset = pd.read_csv('student-math.csv', sep = ';')

#the sum of the respective three grades in the row
dataset['final_grade'] = dataset.apply(lambda row: row.G1 + row.G2 + row.G3, axis=1)
ex_dataset = dataset.copy()

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

#Fitting Linear Regression to Train_Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predict the results
y_pred = np.int64(regressor.predict(X_test))

#Checking the score  
print('Train Score: ', regressor.score(X_train, y_train))  
print('Test Score: ', regressor.score(X_test, y_test))
print('Predict Score: ', regressor.score(X_test, y_pred))

#Visualise
plt.scatter(y_test, y_pred, color='red')
plt.title('y_pred vs y_test')
plt.xlabel('y_test')
plt.ylabel('y_pred')
plt.show() 

#Building optimal model using backward elimination model
import statsmodels.api as sm

def backwardElimination(x, sl):
	numVars = len(x[0])
	for i in range(0, numVars):
		regressor_OLS = sm.OLS(y, x).fit()
		maxVar = max(regressor_OLS.pvalues).astype(float)
		if maxVar > sl:
			for j in range(0, numVars - i):
				if (regressor_OLS.pvalues[j].astype(float) == maxVar):
					x = np.delete(x, j, 1)
	print(regressor_OLS.summary())
	return x

SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]]
X_Modeled = backwardElimination(X_opt, SL)

#Visualisation Insights

#Bar-plot that provide insight how the 'sex' of the students relate their 'final_grade'
sns.barplot(x = 'sex', y = 'final_grade', data = ex_dataset)

#Violin-plots that show relations between how 'address' of students affect their 'final_grade'
sns.violinplot(x = 'address', y = 'final_grade', data = ex_dataset, hue = 'sex')
sns.violinplot(x = 'address', y = 'final_grade', data = ex_dataset, hue = 'sex', split = True)

#lm-plot that provide insights on how 'studytime' of students affects their 'final_grade'
sns.lmplot(x = 'studytime', y = 'final_grade', data = ex_dataset, hue = 'sex', markers = ['o', 'v'])

#lm-plots that provide insights on how 'studytime' of students affects their 'final_grade' differentiated by 'sex'
sns.lmplot(x = 'studytime', y = 'final_grade', data = ex_dataset, hue = 'sex', markers = ['o', 'v'], col = 'sex')

#lm-plots that provide insights on how 'studytime' of students affects their 'final_grade' differentiated by 'sex' with variations of 'school-support' and 'family-support'
sns.lmplot(x = 'studytime', y = 'final_grade', data = ex_dataset, hue = 'sex', markers = ['o', 'v'], col = 'schoolsup', row = 'famsup')
