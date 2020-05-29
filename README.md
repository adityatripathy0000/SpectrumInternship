# Spectrum Data Science and Machine Learning Internship Project Report

## About the Project:

In this project, I have built a **Student Grade Prediction Machine Learning Model** based on the student’s data and previous marks.

I imported different libraries like
    
    1. numpy,
    
    2. pandas,
    
    3. sklearn,
    
    4. statsmodel.api,
    
    5. seaborn.

After that I preprocessed the data in the dataset, and changed the binary valued attributes into 0 or 1, nominal valued attributes into encoded values.
Then used various Machine Learning models like Linear Regression, Decision Tree Regression, Random Forest Regression.
And plotted the various insights from the model, I built.

## Techniques used in Final Task of the internship:

#### 1. Linear Regression

##### Results:

Train Score:  0.97592

Test Score:  0.96157

Predict Score:  0.99778

##### Plot:

![Test Image 7](https://github.com/adityatripathy0000/SpectrumInternship/blob/master/Final_Task/Final_Task_Plot.png)

#### 2. Decision Tree Regression

##### Results:

Train Score:  1.0

Test Score:  0.94715

Predict Score:  1.0

##### Plot:

![Test Image 8](https://github.com/adityatripathy0000/SpectrumInternship/blob/master/Final_Task/Final_Task_Plot_DecisionTree.png)

#### 3. Random Forest Regression

##### Results:

Train Score:  0.99602

Test Score:  0.97113

Predict Score:  0.99743

##### Plot:

![Test Image 9](https://github.com/adityatripathy0000/SpectrumInternship/blob/master/Final_Task/Final_Task_Plot_RandomForest.png)

## Inferences that can be derived from dataset:

#### 1. Bar-plot that provide insight how the 'sex' of the students relate their 'final_grade'
![Test Image 1](https://github.com/adityatripathy0000/SpectrumInternship/blob/master/Final_Task/Insight_Barplot.png)

#### 2. Violin-plots that show relations between how 'address' of students affect their 'final_grade'
![Test Image 2](https://github.com/adityatripathy0000/SpectrumInternship/blob/master/Final_Task/Insight_Violinplot_1.png)

![Test Image 3](https://github.com/adityatripathy0000/SpectrumInternship/blob/master/Final_Task/Insight_Violinplot_2.png)

#### 3. lm-plot that provide insights on how 'studytime' of students affect their 'final_grade'
![Test Image 4](https://github.com/adityatripathy0000/SpectrumInternship/blob/master/Final_Task/Insight_lmplot_1.png)

#### 4. lm-plots that provide insights on how 'studytime' of students affect their 'final_grade' differentiated by 'sex'
![Test Image 5](https://github.com/adityatripathy0000/SpectrumInternship/blob/master/Final_Task/Insight_lmplot_2.png)

#### 5. lm-plots that provide insights on how 'studytime' of students affect their 'final_grade' differentiated by 'sex' with variations of 'school-support' and 'family-support'
![Test Image 6](https://github.com/adityatripathy0000/SpectrumInternship/blob/master/Final_Task/Insight_lmplot_3.png)
