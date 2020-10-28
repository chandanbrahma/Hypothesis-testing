# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:42:51 2020

@author: admin
"""
## importing the dataset
import pandas as pd
data=pd.read_csv('E:\\assignment\\hypothesis\\Cutlets.csv')

## The F&B manager wants to determine whether there is any significant difference in the diameter of the cutlet between two units,
##So from the data we can observe that there is 2 discrete variables and output variable will be continuous. So we will go for 
## 2 sample T test.



## for our analysis lets us take as,
##  Ho= There is no significant difference
##  Ha= There is significant difference

## normalisation test of Y1 and Y2
# for the normalisation test declaring Ho and Ha as,
# Ho= Y1 and Y2 are normal 
# Ha= Y1 and Y2 are nor normal

from scipy import stats
## shapiro test for normalisation
stats.shapiro(data['Unit A']) #pvalue= 0.319
stats.shapiro(data['Unit B']) #pvalue= 0.522

##so from the avove result we can see that p>0.05
## so P high Ho fly, unable to reject Ho, So data is normal


## now checking for the external conditions,
## it is obvious that the external conditions are not same in both the units
## now checking the variance and taking the Ho and Ha for the same
#     Ho= variance are equal
#     Ha= variance are not equal

stats.levene(data['Unit A'], data['Unit B']) #pvalue= 0.417

##p>0.05, so accepting the null hypothesis
## variance are equal

## now finally going for the 2-samole T test for equal variance
stats.ttest_ind(data['Unit A'], data['Unit B']) #pvalue= 0.472

## so we got p value greater than 0.05, hence accepting the null hypothesis
## Hence there is no significant difference between the diameter of the cutlets
