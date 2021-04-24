#Dropout and Batch Normalization

#Dropout - to break conspiracies, network has to search for broad, general patterns whose weight patterns tend to be more robust
#Batch normalization - correct training that is slow or unstable
#					- performs a kind of coordinated rescaling of inputs

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
	layers.Dense(1024, activation = 'relu', input_shape=[11]),
	layers.Dropout(0.3),
	layers.BatchNormalization(),
	layers.Dense(1024, activation = 'relu'),
	layers.Dropput(0.3),
	layers.BatchNormalization(),
	layers.Dense(1024, activation = 'relu'),
	layers.Dropout(0.3),
	layers.BatchNormalization(),
	layers.Dense(1),
])

model.compile(
	optimizer = 'adam',
	loss='mae',
)

history = model.fit(
	X_train, y_train,
	validation_data = (X_valid, y_valid),
	batch_size = 256,
	epochs=100,
	verbose=0,
)

history_df = pd.DataFrame(history.history)
history_df.loc[:, ['loss', 'val_loss']].plot();

