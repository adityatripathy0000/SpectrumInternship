# Spectrum Data Science and Machine Learning Internship Project Report

## About the Project:

In this internship, I have built a **Student Grade Prediction Machine Learning Model Project** based on the student’s data and their previous marks.

I imported different machine learning libraries like:
    
    1. numpy,    
    2. pandas,    
    3. sklearn,
    4. statsmodel.api,    
    5. seaborn.

There I also added the three marks in the subjects of 'G1', 'G2' and 'G3' and initialized the summation of them with another column called as 'final_grade'.

After that, I preprocessed the data in the dataset, and changed the binary valued attributes into 0 or 1, nominal valued attributes into encoded values.

Then used various Machine Learning models like Linear Regression, Decision Tree Regression, Random Forest Regression.

Then plotted the various insights from the model, I built.

And determined various scores of the the regression like:
        
        1. Train Score : Score between X_train, y_train variables,      
        2. Test Score : Score between X_test, y_test variables,      
        3. Predict Score : Score between X_test, y_pred variables.
        
Atlast, in Linear Regression I used Ordinary Least Square(OLS) method for Backward Elimination of the attributes to find out which attributes affected the most.

## Important attributes for affecting prediction of final_grade:
        1. age,
        2. famrel,
        3. absences,
        4. G1,
        5. G2.

## Future Development of the Project:

         1. Develop a web-application using flask api for taking input for the model and predict the output in the html page.
         2. Include a data-base to store the marks of the all the students.
         3. Track progression of the students and distinguish them into categories by their marks and priortise them as per the attention they require.
         4. Track average results progression by school-wise in district-level, state-level, country-level.

## Techniques used in Final Task of the Internship:

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

#### 1. Bar-plot that provide insight how the 'sex' of the students relate their 'final_grade' (i.e Gender factor)
![Test Image 1](https://github.com/adityatripathy0000/SpectrumInternship/blob/master/Final_Task/Insight_Barplot.png)

#### 2. Violin-plots that show relations between how 'address' of students affect their 'final_grade' (i.e School Infrastruture/ teaching quality factor)
![Test Image 2](https://github.com/adityatripathy0000/SpectrumInternship/blob/master/Final_Task/Insight_Violinplot_1.png)

![Test Image 3](https://github.com/adityatripathy0000/SpectrumInternship/blob/master/Final_Task/Insight_Violinplot_2.png)

#### 3. lm-plot that provide insights on how 'studytime' of students affect their 'final_grade' (i.e Hardworking factor)
![Test Image 4](https://github.com/adityatripathy0000/SpectrumInternship/blob/master/Final_Task/Insight_lmplot_1.png)

#### 4. lm-plots that provide insights on how 'studytime' of students affect their 'final_grade' differentiated by 'sex' (i.e Hardworking factor)
![Test Image 5](https://github.com/adityatripathy0000/SpectrumInternship/blob/master/Final_Task/Insight_lmplot_2.png)

#### 5. lm-plots that provide insights on how 'studytime' of students affect their 'final_grade' differentiated by 'sex' with variations of 'school-support' and 'family-support' (i.e Support factor)
![Test Image 6](https://github.com/adityatripathy0000/SpectrumInternship/blob/master/Final_Task/Insight_lmplot_3.png)

### By:
### Aditya Prasad Tripathy
### Regd no. - 1701106508
### Branch - Information Technology
### CET, BBSR
