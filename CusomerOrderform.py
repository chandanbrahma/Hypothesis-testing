##import the dataset
import pandas as pd
data=pd.read_csv('E:\\assignment\\hypothesis\\customerorderform.csv')


##so here we have our business problem is whether the defective %  varies by centre
## we can take our Ho and Ha as followes
##      Ho= percentage does not varies
##      Ha= Percentage varies by centre

## As we have 4 discrete catagorical variables so Chi sruare test will give better result


## Chi-square test
from scipy import stats

data_new=data.apply(pd.value_counts)

Chi_results=stats.chi2_contingency(data_new)

Chi_square=[['','Test Statistic','p-value'],['Sample Data',Chi_results[0],Chi_results[1]]]
Chi_square

## so we got a p value of 0.277.
##hence p>0.05, So fail to reject the null hypothesis
## So the defective percentage is same by the centre at 5% significant level.









