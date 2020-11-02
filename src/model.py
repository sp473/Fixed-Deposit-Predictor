import numpy as np
import pandas as pd

#For plotting
import seaborn as sns
import matplotlib.pyplot as plt


train=pd.read_csv("train2.csv")
test=pd.read_csv("test2.csv")
train.drop(train.columns[0],axis=1,inplace=True)
test.drop(test.columns[0],axis=1,inplace=True)
out=pd.DataFrame()
out=test


train.columns
test.columns


train.shape
test.shape

train.head()

train.isnull().sum()

#UNIVARIATE ANALYSIS
train['subscribed'].value_counts().plot.bar()
train['job'].value_counts().plot.bar()
train['default'].value_counts().plot.bar()
train['marital'].value_counts().plot.bar()
train['education'].value_counts().plot.bar()
train['loan'].value_counts().plot.bar()
train['housing'].value_counts().plot.bar()


#BIVARIATE ANALYSIS
print(pd.crosstab(train['job'],train['subscribed']))
job=pd.crosstab(train['job'],train['subscribed'])
job.div(job.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True, figsize=(8,8))
plt.xlabel('Job')
plt.ylabel('Percentage')


print(pd.crosstab(train['default'],train['subscribed']))
job=pd.crosstab(train['default'],train['subscribed'])
job.div(job.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True, figsize=(8,8))
plt.xlabel('Default')
plt.ylabel('Percentage')


print(pd.crosstab(train['marital'],train['subscribed']))
job=pd.crosstab(train['marital'],train['subscribed'])
job.div(job.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True, figsize=(8,8))
plt.xlabel('Marital')
plt.ylabel('Percentage')


print(pd.crosstab(train['education'],train['subscribed']))
job=pd.crosstab(train['education'],train['subscribed'])
job.div(job.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True, figsize=(8,8))
plt.xlabel('Education')
plt.ylabel('Percentage')


print(pd.crosstab(train['loan'],train['subscribed']))
job=pd.crosstab(train['loan'],train['subscribed'])
job.div(job.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True, figsize=(8,8))
plt.xlabel('Loan')
plt.ylabel('Percentage')


print(pd.crosstab(train['housing'],train['subscribed']))
job=pd.crosstab(train['housing'],train['subscribed'])
job.div(job.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True, figsize=(8,8))
plt.xlabel('Housing Loan')
plt.ylabel('Percentage')


targ=train['subscribed']
train=train.drop('subscribed',axis=1)


train=pd.get_dummies(train)
train.head()


from sklearn.model_selection import train_test_split

x_train,x_val,y_train,y_val=train_test_split(train,targ,test_size=0.2)

from sklearn.linear_model import LogisticRegression

lr=LogisticRegression()
lr.fit(x_train,y_train)
pred=lr.predict(x_val)

from sklearn.metrics import  accuracy_score

accuracy_score(y_val,pred)

from sklearn.tree import DecisionTreeClassifier

clf=DecisionTreeClassifier(max_depth=6,random_state=0)

clf.fit(x_train,y_train)

predict=clf.predict(x_val)

accuracy_score(y_val,predict)


test=pd.get_dummies(test)

test_prediction=clf.predict(test)

submission=pd.DataFrame()


submission['ID']=test['ID']
submission['subscribed']=test_prediction


submission.replace(0,'No',inplace=True)
submission.replace(1,'Yes',inplace=True)


submission.to_csv('predicted.csv',header=True,index=False)


output=pd.DataFrame('predicted.csv')
output.head()
