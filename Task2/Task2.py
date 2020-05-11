#Import_Library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Import_Dataset
dataset = pd.read_csv('student-math.csv')

#the sum of the respective three grades in the row
dataset['final_grade'] = dataset.apply(lambda row: row.G1 + row.G2 + row.G3, axis=1)

#Delete the three grades from the dataframe
del dataset['G1']
del dataset['G2']
del dataset['G3']

#Replace all binary values with 1 and 0 in the dataframe
X = dataset.values
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
X[:,15] = labelencoder_X.fit_transform(X[:,15])
X[:,16] = labelencoder_X.fit_transform(X[:,16])
X[:,17] = labelencoder_X.fit_transform(X[:,17])
X[:,18] = labelencoder_X.fit_transform(X[:,18])
X[:,19] = labelencoder_X.fit_transform(X[:,19])
X[:,20] = labelencoder_X.fit_transform(X[:,20])
X[:,21] = labelencoder_X.fit_transform(X[:,21])
X[:,22] = labelencoder_X.fit_transform(X[:,22])

#variable for visualization
studytime = dataset['studytime']
final_grade = dataset['final_grade']

#Visualize scatter-plot
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

plt.scatter(studytime, final_grade, c = cols)
plt.title('Studytime Vs. Final_Grade')
plt.xlabel('Studytime')
plt.ylabel('Final_Grade')
plt.show()

#Visualize box-plot
sns.boxplot(x = studytime, y = final_grade)