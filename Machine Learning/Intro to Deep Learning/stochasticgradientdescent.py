import pandas as pandas
from IPython.display import display

red_wine = pd.read_csv('../input/dl-course-data/red-wine.csv')

# Create training and validation splist
df_train = red_wine.sample(frac=0.7, random_state=0)
df_valid = red_wine.drop(df_train.index)
display(df_train.head(4))

# Scale to [0,1]
max_ = df_train.max(axis = 0)
min_ = df_train.min(axis=0)
df_train = (df_train - min_) / (max_ - min_)
df_valid = (df_valid - min_) / (max_ - min_)

# Split features and target
X_train = df_train.drop('quality', axis = 1)
X_valid = df_valid.drop('quality', axis = 1)
y_train = df_train['quality']
y_valid = df_valid['quality']

print(X_train.shape)

#3 layer network, 1500 neurons

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
	layers.Dense(512, activation = 'relu', input_shape=[11]),
	layers.Dense(512, activation = 'relu'),
	layers.Dense(512, activation = 'relu'),
	layers.Dense(1),
])

# Defines the model
model.compile(
	optimizer='adam',
	loss='mae',
)

history = model.fit(
	X_train, y_train,
	validation_data=(X_valid, y_valid),
	batch_size = 256,
	epochs=10,
)

import pandas as pf

#convert the training history to a dataframe
history_df = pd.DataFrame(history.history)
#use pandas native plot method
history_df['loss'].plot();

#Exercise

import numpy as np 
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_transformer, make_column_selector
from sklearn.model_selection import train_test_split

fuel = pd.read_csv('../input/dl-course-data/fuel.csv')

X = fuel.copy()
#Remove target
y = X.pop('FE')

preprocessor = make_column_transformer(
	(StandardScaler(),
	make_column_selector(dtype_include=np.number)),
	(OneHotEncoder(sparse=False),
	make_column_selector(dtype_include=object)),
)

X = preprocessor.fit_transform(X)
y = np.log(y) # log transform target instead standardizing

input_shape = [X.shape[1]]
print("Input shape: {}".format(input_shape))

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
	layers.Dense(128, activation = 'relu', input_shape=input_shape),
	layers.Dense(128, activation = 'relu'),
	layers.Dense(64, activation = 'relu'),
	layers.Dense(1),
])

#Add Loss and optimizer
model.compile(
	optimizer = 'adam',
	loss = 'mae',
)

#Train model
history = model.fit(
	X,y,
	batch_size = 128,
	epochs = 200,
)

#Look at loss curves and evaluate training dataframe

import pandas as pd
history_df = pd.DataFrame(history.history)
#Starts the plot at epoch 5
history_df.loc[5:, ['loss']].plot();

#With learning rate and batch size, we have some control over:
# 1) How long it takes to train a model
# 2) How noise the learning curves are
# 3) How small the loss becomes

# learning_rate = 0.05, the bigger the more abrupt/vary training loss and weights
#batch_size = 128, the lesser, takes longer to get the best loss

# Smaller batch size gave noisier weight updates and loss curves
# smaller learning rates make the updates smaller and training data takes longer to converge
# Large learning rates can speed up training, but if too large, training can fail