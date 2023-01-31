# first neural network with keras tutorial
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
# mlp for regression with mse loss function
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from matplotlib import pyplot
import keras_tuner

def postprocessing():
    data = pd.read_csv('processed_data.csv', sep=',')
    data.drop(columns=['tconst'],inplace=True)
    data.dropna(subset=['genre_1'])
    data.drop(columns=['crew_7','crew_8','crew_9','crew_10'],inplace=True)
    data.drop(columns=['crew_6','crew_5','crew_4','crew_3','crew_2','crew_1'],inplace=True)
    # data.drop(columns=["genre_1",'genre_2','genre_3'],inplace=True)
    # data['genre_1'] = data['genre_1'].replace(r'\\N','0',regex=True)
    data['startYear'] = data['startYear'].replace(r'\\N','0',regex=True)
    data.drop(data[data["startYear"] =="0"].index, inplace = True)
    data.drop(data[data["genre_1"] == "0"].index, inplace = True)

    data = pd.get_dummies(data, columns=['genre_1','genre_2','genre_3'])
    # print(data)
    data.to_csv('postprocessed_data.csv',index=False)    # zapisanie danych preprocessed dataframe do pliku


# postprocessing()
def build_model(hp):

    # define the keras model
    model = Sequential()
    # model.add(layers.Dense(units=hp.Int("units", min_value=32,max_value=512,step=32), activation=hp.Choice("activation", ["relu", "linear"])))
    # Tune whether to use dropout.
    for i in range(hp.Int("num_layers", 1, 3)):
        model.add(
            layers.Dense(
                # Tune number of units separately.
                units=hp.Int(f"units_{i}", min_value=32, max_value=512, step=32),
                activation=hp.Choice("activation", ["relu", "linear"]),
            )
        )
    if hp.Boolean("dropout"):
        model.add(layers.Dropout(rate=0.25))
    # model.add(Dense(128, input_dim=85, activation='relu', kernel_initializer='he_uniform'))
    # model.add(Dense(256, activation='relu'))
    model.add(Dense(1, activation='linear'))

    # compile the keras model
    # print("\n\nCompiling keras model\n\n")
    learning_rate = hp.Float("lr", min_value=1e-5, max_value=1e-2, sampling="log")
    model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate,clipnorm=0.1), metrics=[keras.metrics.MeanSquaredError()])

    return model


tuner = keras_tuner.RandomSearch(
    hypermodel=build_model,
    objective="mean_squared_error",
    max_trials=10,
    executions_per_trial=3,
    overwrite=True,
    directory="my_dir",
    project_name="helloworld",
)

data = pd.read_csv('postprocessed_data.csv', sep=',')
data = data.fillna(0)
# print(data)

# split into train and test
data_train, data_test = train_test_split(data, test_size=0.2)

data_train = data_train.to_numpy()
data_test = data_test.to_numpy()

trainX = data_train[:,1:]
x_val = data_train[:,1:]

trainy = data_train[:,0]
y_val = data_train[:,0]

testX = data_test[:,1:]
testy = data_test[:,0]

build_model(keras_tuner.HyperParameters())
tuner.search(trainX, trainy, epochs=50,batch_size=512, validation_data=(x_val, y_val))

best_hps = tuner.get_best_hyperparameters(5)
# Build the model with the best hp.
model = build_model(best_hps[0])

model.fit(x=trainX, y=trainy, epochs=1)

# # fit the keras model on the dataset
# print("fitting keras model")
# history = model.fit(trainX, trainy, validation_data=(testX, testy), epochs=250, batch_size=512)

# # evaluate the keras model
# print("evaluating keras model")
# train_mse = model.evaluate(trainX, trainy, verbose=0)
# test_mse = model.evaluate(testX, testy, verbose=0)
# print('Train: %.3f, Test: %.3f' % (train_mse, test_mse))


# # plot loss during training
# pyplot.title('Loss / Mean Squared Error')
# pyplot.plot(history.history['loss'], label='train')
# pyplot.plot(history.history['val_loss'], label='test')
# pyplot.legend()
# pyplot.show()

# predictions = model.predict(testX)
# # show the inputs and predicted outputs
# for i in range(10):
# 	print('got %f (expected %.1f)' % (predictions[i], testy[i]))