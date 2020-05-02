import tensorflow as tf
# https://colab.research.google.com/github/google/eng-edu/blob/master/ml/cc/exercises/linear_regression_with_synthetic_data.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=linear_regression_synthetic_tf2-colab&hl=en#scrollTo=_GMGgR6O54IN
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def build_model(my_lr):
    model = tf.keras.models.Sequential()
    
    # define topology here
    model.add(tf.keras.layers.Dense(units=1, input_shape=(1,)))
    # choose optimizers and loss function here
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=my_lr, loss='mean_squared_error', metrics=[tf.keras.metrics.RootMeanSquaredError()])
    return model

def train_model(model, feature, label, epochs, batch_size):
    history = model.fit(x=feature, y=label, batch_size=batch_size, epochs=epochs, verbose=1)
    [trained_w, trained_b] = model.get_weights()
    epochs = history.epoch      
    rmse = pd.DataFrame(history.history)['root_mean_squared_error']
    return trained_w, trained_b, epochs, rmse
                  
