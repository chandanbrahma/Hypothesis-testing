##importing the data
import pandas as pd
data= pd.read_csv('E:\\assignment\\hypothesis\\Faltoons.csv')

##we can see the data has 2 discrete input variable. So 2 propertion test will give us better result
##now lets take the null and absolute hypothesis
# Ho= no of males and female walking are same
# Ha= no of males and females are not same 
crosstab= pd.crosstab(data['Weekdays'],data['Weekend'])
crosstab
data_new=data.apply(pd.value_counts)
data_new


n1=233
p1=0.448
n2=167
p2=0.596
import numpy as np
population1=np.random.binomial(1, p1, n1)
population2=np.random.binomial(1,p2,n1)


##applying on the population 

import statsmodels.api as sm
sm.stats.ttest_ind(population1,population2)#p=0.002
## so as p<0.05, Hence rejecting the null hypothesis
## so no of males and females are not same
##now lets predict wheather males are higher than female or not, for the same lets take our Ho and Ha

#  Ho= no of female are smaller than male
#  Ha= no of female are not smaller than male


sm.stats.ttest_ind(population1,population2,alternative='smaller') #p=0.001
 ## As we got a lower p value so rejecting the null hypothesis and hence concluding
 ## propertion of female is greater than male.