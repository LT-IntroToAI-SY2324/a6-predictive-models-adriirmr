import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''
**********CREATE THE MODEL**********
'''

data = pd.read_csv("data.csv")
x = data["Age"].values 
y = data["Blood Pressure"].values

# Create your training and testing datasets:
print(f"x {x}") 
print(f"y {y}")
print(f"xtrain {xtrain}")
print(f"xtest {xtest}")
print(f"ytrain {ytrain}")
print(f"ytest {ytest}") 

# Use reshape to turn the x values into 2D arrays:
xtrain = xtrain.reshape(-1,1)

# Create the model
model = LinearRegression().fit(xtrain, ytrain) 

# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 
coef =round(float(model.coef_), 2)
intercept = round (float(model.intercept_) 2)
r_squared = model.score(xtrain, ytrain)

# Print out the linear equation and r squared value:

'''
**********TEST THE MODEL**********
'''
# reshape the xtest data into a 2D array

# get the predicted y values for the xtest values - returns an array of the results

# round the value in the np array to 2 decimal places


# Test the model by looping through all of the values in the xtest dataset
print("\nTesting Linear Model with Testing Data:")


'''
**********CREATE A VISUAL OF THE RESULTS**********
'''
