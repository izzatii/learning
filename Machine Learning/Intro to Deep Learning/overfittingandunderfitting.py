#Underfitting - loss is not low as it could be because model hasn't learned enought signal
#Overfitting - loss is not as low as it could because the model learned too much noise

#The trick is to find best balance between the two
# Look at couplde of was to get  more signal out of training data while reduce amount of noise

#Capacity - size and complexity of pattern able to learn - how many neurons it has and how they are connected together
# 			1) wider - more units to existing layer (better for linear)
#			2) deeper - add more layers (better for non-linear)

model = keras.Sequential([
	layers.Dense(16, activation='relu'),
	layers.Dense(1),
])

wider = keras.Sequential([
	layers.Dense(23, activation='relu'),
	layers.Dense(1),
])

deeper = keras.Sequential([
	layers.Dense(16, activation='relu'),
	layers.Dense(16, activation='relu'),
	layers.Dense(1),
])

#Early stopping - once detect validation loss starting to rise again, reset weights back to wehere the minimum occured. 
#Ensures model won't continue to learn noise and overfit data
#Early stopping though callback

from tensorflow.keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(
	min_delta = 0.001, #minimum amount of change to count as an improvement
	patience = 20, #how many epochs to wait before stopping
	restore_best_weights = True,
)

##---continue from previous
from tensorflow import keras
from tensorflow.keras import layers, callbacks

early_stopping = callbacks.EarlyStopping(
	min_delta = 0.001,
	patience = 20,
	restore_best_weights = True,
)

model = keras.Sequential([
	layers.Dense(512, activation='relu', input_shape=[11]),
	layers.Dense(512, activation='relu'),
	layers.Dense(512, activation='relu'),
	layers.Dense(1),
])

model.compile(
	optimizer = 'adam',
	loss = 'mae',
)

history = model.fit(
	X_train, y_train,
	validation_data = (X_valid, y_valid),
	batch_size = 256,
	epochs=500,
	callbacks=[early_stopping],
	verbose=9, #turn off training log
)

history_df = pd.DataFrame(history.history)
history_df.loc[:, ['loss','val_loss']].plot();
print("Minimum validation loss : {}".format(history_df['val_loss'].min()))

#Exercise

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.model_selection import GroupShuffleSplit

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import callbacks

spotify = pd.read_csv('../input/dl-course-data/spotify.csv')

X = spotify.copy().dropna()
y = X.pop('track_popularity')
artists = X['track_artist']

features_num = ['danceability', 'energy', 'key', 'loudness', 'mode',
				'speedhiness', 'accousticness', 'instrumentalness',
				'liveness', 'valence', 'tempo', 'duration_ms']

features_cat = ['playlist_genre']

preprocessor = make_column_transformer(
	(StandardScaler(), features_num),
	(OneHotEncoder(), features_cat),
)

def group_split(X, y, group, train_size = 0.75):
    splitter = GroupShuffleSplit(train_size=train_size)
    train, test = next(splitter.split(X, y, groups=group))
    return (X.iloc[train], X.iloc[test], y.iloc[train], y.iloc[test])

	X_train, X_valid, y_train, y_valid = group_split(X, y, artists)

	X_train = preprocessor.fit_transform(X_train)
	X_valid = preprocessor.transform(X_valid)
	y_train = y_train / 100 # popularity is on a scale 0-100, so this rescales to 0-1.
	y_valid = y_valid / 100

	input_shape = [X_train.shape[1]]
	print("Input shape: {}".format(input_shape))

model = keras.Sequential([
    layers.Dense(1, input_shape=input_shape),
])

model.compile(
    optimizer='adam',
    loss='mae',
)

history = model.fit(
    X_train, y_train,
    validation_data=(X_valid, y_valid),
    batch_size=512,
    epochs=50,
    verbose=0, # suppress output since we'll plot the curves
)

history_df = pd.DataFrame(history.history)
history_df.loc[0:, ['loss', 'val_loss']].plot()
print("Minimum Validation Loss: {:0.4f}".format(history_df['val_loss'].min()));
# Start the plot at epoch 10
history_df.loc[10:, ['loss', 'val_loss']].plot()
print("Minimum Validation Loss: {:0.4f}".format(history_df['val_loss'].min()));

model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=input_shape),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
])
model.compile(
    optimizer='adam',
    loss='mae',
)
history = model.fit(
    X_train, y_train,
    validation_data=(X_valid, y_valid),
    batch_size=512,
    epochs=50,
)
history_df = pd.DataFrame(history.history)
history_df.loc[:, ['loss', 'val_loss']].plot()
print("Minimum Validation Loss: {:0.4f}".format(history_df['val_loss'].min()));

from tensorflow.keras import callbacks

# YOUR CODE HERE: define an early stopping callback
early_stopping = callbacks.EarlyStopping(
    min_delta = 0.001,
    patience = 5,
    restore_best_weights = True,
)

model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=input_shape),
    layers.Dense(64, activation='relu'),    
    layers.Dense(1)
])
model.compile(
    optimizer='adam',
    loss='mae',
)
history = model.fit(
    X_train, y_train,
    validation_data=(X_valid, y_valid),
    batch_size=512,
    epochs=50,
    callbacks=[early_stopping]
)
history_df = pd.DataFrame(history.history)
history_df.loc[:, ['loss', 'val_loss']].plot()
print("Minimum Validation Loss: {:0.4f}".format(history_df['val_loss'].min()));


