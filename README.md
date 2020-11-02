# Fixed-Deposit-Predictor

A predictive model which predicts if a customer will subscribe to a Fixed Deposit based on his financial and personal status. This model is implented using the python language.
The data-set used to train this model, has the following columns/features.

This is a classification problem, that predicts if a customer will subscribe to a term deposit based on his personal data, given below.


VARIABLE - DEFINITION

1.Id	      -  Unique id of client

2.age	      -  Age of client

3.Job	      -  Job of the client

4.Marital   -	 Marital status of the client

5.Education	-  Education of client

6.Default	  -  Credit in default(yes/no). Tells us if the customer has any unpaid loans.

7.Housing	  -  Housing loan(yes/no). Tells us if the customer has taken a housing loan in the past.


8.Loan	    -  Personal loan(yes/no). Tells us if the customer has taken a personal loan in the past.

9.Subscribed(target variable) -	Has the client subscribed to the term deposit.

From the dataset the first 8 columns(variables) are the predictor variables, and the final column is the target variable. Using a training data set the model is trained, and the testing data set is used to test the performance of the model when it's given unseen data. 



The first 5 rows of the data set looks something like this.

![](SCREENSHOTS/first5rows.png)


Results of bivariate analysis. Here I compared 2 variables. One predictor variable and one target variable. 
I've analysed the relation ships between the following 5 sets of variables.

1. Education of the customer and Subscribed(target variable)
2. Default status of the customer and Subscribed(target variable)
3. Housing loan history of customer and Subscribed.
4. Personal loan history of customer and Subscribed.
5. Martial status of customer and Subscribed.

 
 
 ![](SCREENSHOTS/edu_subscribed.png)
 


 
 ![](SCREENSHOTS/defualt_subscribed.png)




 ![](SCREENSHOTS/housing_subscribed.png)
 

 ![](SCREENSHOTS/loan_subscribed.png)
 
 
 ![](SCREENSHOTS/job_subscribed.png)
 

 ![](SCREENSHOTS/marital_subscribed.png)


For the predictive model I initially used the linear regression model , and I got an accuracy of 85.1%. Then later i used the decision tree model object, and my accuracy of the model went up to 88.56%.



The first 5 rows of the testing data set before the prediction was made by the model.

 ![](SCREENSHOTS/first5rowstest.png)
 
 
 The first 5 rows of the testing data set after the prediction has been made.
 ![](SCREENSHOTS/first5rowstest2.png)
