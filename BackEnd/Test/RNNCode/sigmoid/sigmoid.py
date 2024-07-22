import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('DATA\\RNN Data\\final.csv')

# One-hot encode categorical columns
encoder = OneHotEncoder(sparse=False, drop='first')  # Drop first to avoid multicollinearity
categorical_cols = ['Social Category', 'Income']
encoded_categorical = encoder.fit_transform(data[categorical_cols])

# Normalize numerical columns
scaler = MinMaxScaler()
numerical_cols = ['prim_Girls', 'prim_Boys', 'prim_Overall', 'upPrim_Girls', 'upPrim_Boys', 'upPrim_Overall', 'snr_Girls', 'snr_Boys', 'snr_Overall']
normalized_numerical = scaler.fit_transform(data[numerical_cols])

# Combine all features
features = np.hstack([encoded_categorical, normalized_numerical])

# Create target column for dropout
data['dropout'] = (data['snr_Overall'] > 0).astype(int)

# Split data into features and target
X = features
y = data['dropout'].values

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define RNN model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),
    tf.keras.layers.Reshape((X_train.shape[1], 1)),  # Reshape for RNN input
    tf.keras.layers.SimpleRNN(50, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # Output layer with sigmoid for binary classification
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=150, batch_size=32, validation_split=0.2)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Loss: {loss:.4f}')
print(f'Accuracy: {accuracy*100:.2f}%')

# Predict on test set
predictions = model.predict(X_test)
predictions = (predictions > 0.5).astype(int)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy (manual): {accuracy*100:.2f}%')

# Plot learning curves
plt.figure(figsize=(12, 6))

# Plot training & validation loss values
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

# Plot training & validation accuracy values
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.show()


model.save('BackEnd\\Test\\RNNCode\\sigmoid\\rnn_model.h5')