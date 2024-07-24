from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow as tf
import sklearn as scikit
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN, ReLU, Softmax

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Load the CSV data
data = pd.read_csv('DATA\\RNN Data\\final.csv')

# Display the original data
print("Original Data:")
print(data.head())

# Initialize the OneHotEncoder
encoder = OneHotEncoder(sparse=False)

# One-hot encode 'Social Category' and 'Income'
encoded_columns = encoder.fit_transform(data[['Social Category', 'Income']])

# Create a DataFrame with the encoded columns
encoded_df = pd.DataFrame(encoded_columns, columns=encoder.get_feature_names_out(['Social Category', 'Income']))

# Concatenate the original DataFrame (excluding the encoded columns) with the encoded DataFrame
normalized_data = pd.concat([data.drop(columns=['Social Category', 'Income']), encoded_df], axis=1)

# Display the normalized data
print("\nNormalized Data:")
print(normalized_data.head())

# Save the normalized data to a new CSV file
normalized_data.to_csv('DATA\\RNN Data\\normalized_data.csv', index=False)

# Assuming normalized_data is already loaded and preprocessed
# Split data into features and labels (assuming labels are in the last column for this example)
features = normalized_data.drop(columns=['DNo', 'District']).values
labels = normalized_data['snr_Overall'].values

# Reshape features for RNN input (samples, timesteps, features)
# Here, we'll treat each row as a separate sequence of 1 timestep
features = features.reshape((features.shape[0], 1, features.shape[1]))

# Define the RNN model
model = Sequential()
model.add(SimpleRNN(units=50, input_shape=(features.shape[1], features.shape[2])))
model.add(ReLU())
model.add(Dense(units=labels.max() + 1))  # Assuming labels are categorical
model.add(Softmax())

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model (assuming a simple train/test split)
history = model.fit(features, labels, epochs=150, batch_size=32, validation_split=0.2)

# Plot the learning curve
plt.figure(figsize=(12, 6))

# Plot training & validation loss values
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Learning Curve - Loss')
plt.legend(loc='upper right')
plt.show()

# Optionally, plot training & validation accuracy values if available
if 'accuracy' in history.history:
    plt.figure(figsize=(12, 6))
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.title('Learning Curve - Accuracy')
    plt.legend(loc='lower right')
    plt.show()


# Get the impression values (predicted probabilities) for the training data
impressions = model.predict(features)

# Print the impression values
print("\nImpression Values:")
print(impressions)

# Save the model
model.save('BackEnd\\Test\\RNNCode\\softmax\\rnn_model.h5')

# Evaluate the model on the test data
test_loss, test_accuracy = model.evaluate(features, labels)

# Print the test accuracy
print("Test Accuracy:", test_accuracy*100)

