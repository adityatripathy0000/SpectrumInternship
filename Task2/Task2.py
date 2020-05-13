#Import_Library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Import_Dataset
dataset = pd.read_csv('student-math.csv', sep = ';')

#the sum of the respective three grades in the row
dataset['final_grade'] = dataset.apply(lambda row: row.G1 + row.G2 + row.G3, axis=1)

#Delete the three grades from the dataframe
dataset = dataset.drop(['G1', 'G2', 'G3'], axis = 1)

#Encode all binary values with 1 and 0 in the dataframe
from sklearn.preprocessing import LabelEncoder
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

#variable for visualization
studytime = dataset['studytime']
final_grade = dataset['final_grade']

#Visualize Scatter-Plot and Box-plot 
def pltcolor(lst):
    cols=[]
    for l in lst:
        if l==1:
            cols.append('blue')
        elif l==2:
            cols.append('orange')
        elif l==3:
            cols.append('green')
        else:
            cols.append('red')
    return cols
cols=pltcolor(studytime)
dataset.boxplot(by = 'studytime', column = 'final_grade', grid = False)
plt.scatter(studytime, final_grade, s = 1, c = cols)
plt.xlabel('Studytime (in Hours)')
plt.ylabel('Final_Grade')
plt.show()