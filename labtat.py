# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:38:36 2020

@author: admin
"""

##importing the data
import pandas as pd
data= pd.read_csv('E:\\assignment\\hypothesis\\LabTAT.csv')

##So as per our business problem we have to find wheather there is any difference in the average Turn Around Time (TAT) of reports of the laboratories on their preferred list.
## in our data set we do have 4 discrete variable and output variable will be continuous. so inthis scenareo one way ANNOVA test will give a better result
 

## now lets choose our null and alternative hypothesis
##          Ho= There is no diffference in the TAT of the reports of the laboratory
##          Ha= There is a difference in the TAT of the reports
 
 
## now lets first check the normality of the data 
##choosing the null and alternative hypothesis as
    # Ho= data are normal
    # Ha= data are not normal

from scipy import stats
stats.shapiro(data['Laboratory 1']) #p =0.550
stats.shapiro(data['Laboratory 2']) #p= 0.863
stats.shapiro(data['Laboratory 3']) #p= 0.420
stats.shapiro(data['Laboratory 4']) #p= 0.661

##so from the shapiro test we can clearly see p >0.05 for all the variables, hence accepting the Ho
## sa data are normal

##now checking the variables
# Ho= variables are equal
# Ha= variables are not equal

stats.levene(data['Laboratory 1'], data['Laboratory 2'],data['Laboratory 3'],data['Laboratory 4'])

#p value is 0.051, hence accepting null hypothesis, so variance are equal

##one way ANOVA test

import statsmodels.api as sm

from statsmodels.formula.api import ols
##replacing the column names
data.columns= ['lab1','lab2','lab3','lab4']
data_ols=ols('lab1~lab2+lab3+lab4',data=data).fit()
anova_table=sm.stats.anova_lm(data_ols,type=2)
print(anova_table)


## So from the ANOVA test we can see the the p values are greater than 0.05, hence accepting our null hypothesis.

## so we can colclude that There is no diffference in the TAT of the reports of the laboratory.
