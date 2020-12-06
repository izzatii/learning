import pandas as pd 
melbourne_file_path = ''
merlbourne_data = pd.read_csv(melbourne_file_path)
melbourne_data.columns
melbourne_data.describe()

#drop missing values
melbourne_data = melbourne_data.dropna(axis=0)

#Prediction Target [y]
#Features = column input in model to make predictions [x]

y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Latitude', 'Longitude']
x = melbourne_data[melbourne_features]

####################################################################################################
#Bulding Models: 
#1) Define: What model to use 
#2)Fit: Capture patterns from data 
#3)Predict 
#4)Evaluate
####################################################################################################

from sklearn.tree import DecisionTreeRegressor
#Define model. Specifiy a number for random_state to ensure same results
melbourne_data = DecisionTreeRegressor(random_state=1)

#Fit model
melbourne_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_data.predict(X.head()))

#######################################################################
#Model Validation = Mean Absoulte Error(MAE): Error = Actual-Predicted
#On average, our predictions are off by about X.

import pandas as pd
#Load data
melbourne_file_path = ''
melbourne_data = pd.read_csv(melbourne_file_path)
#Filter rows with missing price values
filtered_melbourne_data = melbourne_data.dropna(axis=0)
#Choose target and features
y = filtered_melbourne_data.Price
melbourne_features = ['Rooms','Bathroom','Landsize','BuildingArea','YearBuilt','Latitude','Longitude']
X = filtered_melbourne_data[melbourne_features]

from sklearn.tree import DecisionTreeRegressor
#Define model
melbourne_model = DecisionTreeRegressor()
#Fit model
melbourne_model.fit(X,y)

from sklearn.metrics import mean_absolute_error
predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)

#train_test_split = to break up data into two pieces - use some as training data, some to validate data
from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
melbourne_model = DecisionTreeRegressor()
melbourne_model.fit(train_X, train_y)
#get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))

#comparing prediction vs Actual
print("First in-sample predictions:", iowa_model.predict(X.head()))
print("Actual target values for those homes:", y.head().tolist())


from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
iowa_model = DecisionTreeRegressor(random_state=1)
iowa_model.fit(train_X, train_y)

from sklearn.metrics import mean_absolute_error
val_mae = mean_absolute_error(val_y, val_predictions)
print(val_mae)

##############################
#Underfitting and Overfitting
##############################

#Overfitting = model match training data almost perfectly but does poorly in validation and other new data (too many splits)
#				capturing spurious patterns that won't recur in the future, leading to less accurate predictions
#
#Underfitting = model fails to capture important distinctions and patterns in data - tree too shallow, not enough splits
#				failing to capture relevant patterns, again leading to less accurate predictions
#				
#max_leaf_nodes = way to control overfitting vs underfitting

from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
	model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
	model.fit(train_X, train_y)
	preds_val = model.predict(val_X)
	mae = mean_absolute_error(val_y,preds_val)
	return(mae)

#compare MAE with differing values of max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
	my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
	print("Max leaf nodes: %d \t\t Mean Absoulute Error: %d" %(max_leaf_nodes, my_mae))

#---------------

import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

iowa_file_path =''
home_data = pd.read_csv(iowa_file_path)
#create target object
y = home_data.SalePrice
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
#create X
X = home_data[features]
#split validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
#specify odel
iowa_model = DecisionTreeRegressor(random_state=1)
#fitmodel
iowa_model.fit(train_X, train_y)
#make validation predictions and calculate mean absolute error
val_predictions = iowa_model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE: {:,.0f".format(val_mae))

def get_mae(max_leaf_nodes, train_X, val_X, val_y):
	model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
	model.fit(train_X, train_y)
	preds_val = model.predict(val_X)
	mae = mean_absolute_error(val_y, preds_val)
	return(mae)

candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
#write loop to find the ideal tree size from candidate_max_leaf_nodes
for max_leaf_nodes in candidate_max_leaf_nodes:
	my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
	print("Max leaf nodes: %d \t\t Mean Absolute Error: %d" %(max_leaf_nodes, my_mae)

final_model = DecisionTreeRegressor(max_leaf_nodes=100, random_state=0)
final_model.fit(X,y)
#-----------

###################
# Random Forests
###################
#Random forest uses many trees and it makes a prediction by averaging the predictions of each component tree

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))

###############
# Competitions
###############

Features = ['Id', 'MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street',
       'Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig',
       'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType',
       'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd',
       'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType',
       'MasVnrArea', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual',
       'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1',
       'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating',
       'HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF',
       'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath',
       'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual',
       'TotRmsAbvGrd', 'Functional', 'Fireplaces', 'FireplaceQu', 'GarageType',
       'GarageYrBlt', 'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual',
       'GarageCond', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF',
       'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'PoolQC',
       'Fence', 'MiscFeature', 'MiscVal', 'MoSold', 'YrSold', 'SaleType',
       'SaleCondition'],

Features = ['LotArea', 'OverallCond', 'OverallQual', 'YearBuilt', 'YearRemodAdd', 'Heating', 'FullBath', 
			'HalfBath', 'BedroomAbvGr', 'KitchenQual', 'TotRmsAbvGrd', 'Fireplaces', 'GarageArea',
			'GarageCond', 'PoolArea', 'YrSold']