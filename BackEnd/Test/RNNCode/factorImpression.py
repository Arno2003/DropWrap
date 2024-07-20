import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN
from tensorflow.keras.utils import to_categorical

# Generating sample data
np.random.seed(42)
data = np.random.randn(100, 5)
labels = np.random.randint(0, 2, 100)
df = pd.DataFrame(data, columns=['Factor1', 'Factor2', 'Factor3', 'Factor4', 'Factor5'])
df['Dropout'] = labels

# # Display the first few rows of the dataset
# print(len(df))
# print(df.head())

# Prepare the data
X = df.drop('Dropout', axis=1).values
y = df['Dropout'].values

# Convert labels to categorical
y_categorical = to_categorical(y, num_classes=2)

# Reshape input to be [samples, time steps, features]
X_reshaped = X.reshape((X.shape[0], 1, X.shape[1]))

# Build the RNN model
model = Sequential()
model.add(SimpleRNN(10, input_shape=(1, 5), activation='relu'))
model.add(Dense(5, activation='softmax'))  # Output layer for each factor

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_reshaped, X, epochs=10, batch_size=10, verbose=1)

# Predict probabilities for each factor contributing to dropout
predictions = model.predict(X_reshaped)

# Print the first few predictions
for i in range(5):
    print(f"Input Factors: {X[i]}, Factor Probabilities: {predictions[i]}")
