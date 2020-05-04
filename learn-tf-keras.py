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

# Hyperparameters: learning rate, batch size, number of epochs
# Training the model: tune and find a convergence point for loss value
# Loss value:
# 1. doesn't converge, more epochs
# 2. decrease too slowly, increase learning rate (or lower the training loss)
# 3. vary wildly(jumping up and down), decrease learning rate (or increase batch size)
# Commonly good combination: increase epochs/batch size and lower learning rate

def train_model(model, feature, label, epochs, batch_size):
    history = model.fit(x=feature, y=label, batch_size=batch_size, epochs=epochs, verbose=1)
    [trained_w, trained_b] = model.get_weights()
    epochs = history.epoch      
    rmse = pd.DataFrame(history.history)['root_mean_squared_error']
    return trained_w, trained_b, epochs, rmse
                  
def plot_model_fitting(trained_w, trained_b, feature_val, label):
    '''
    plot how the trained model fits the true data
    '''
    plt.xlabel('feature') # only one feature
    plt.ylabel('label')

    plt.scatter(feature_val, label) # true data points
    x = feature_val[-1]
    y = trained_w * x + trained_b
    plt.plot([0, x], [trained_b, y], color='r')    
    plt.show()

def plot_loss(epochs, rmse):
    plt.xlabel('number of epochs')
    plt.ylabel('root mean squared error')
    plt.plot(epochs, rmse, label='loss')
    plt.legend()
    plt.show()
