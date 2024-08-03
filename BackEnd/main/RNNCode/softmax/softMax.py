import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping
import os

def preprocess_data(data: pd.DataFrame, colName: str):
    # One-hot encode categorical columns
    encoder = OneHotEncoder(sparse=False, drop='first')  # Drop first to avoid multicollinearity
    categorical_cols = ['Social Category', 'Income']
    encoded_categorical = encoder.fit_transform(data[categorical_cols])

    # Normalize numerical columns
    scaler = MinMaxScaler()
    normalized_numerical = scaler.fit_transform(data[[colName]].values.reshape(-1, 1))

    # Combine all features
    features = np.hstack([encoded_categorical, normalized_numerical])

    # Create target column for dropout (one-hot encoding)
    data['dropout'] = (data[colName] > 0).astype(int)
    y = pd.get_dummies(data['dropout']).values  # Convert to one-hot encoded format

    return features, y, data

def build_model(input_shape):
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(input_shape,)),
        tf.keras.layers.Reshape((input_shape, 1)),  # Reshape for RNN input
        tf.keras.layers.SimpleRNN(50, activation='relu'),
        tf.keras.layers.Dense(2, activation='softmax')  # Output layer with softmax for binary classification
    ])
    
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def train_and_evaluate(features, y, data, colName, model_dir):
    # Split data into features and target
    X_train, X_test, y_train, y_test = train_test_split(features, y, test_size=0.2, random_state=42)

    # Build the RNN model
    model = build_model(X_train.shape[1])

    # Use early stopping to prevent overfitting
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

    # Train the model
    history = model.fit(X_train, y_train, epochs=60, batch_size=32, validation_split=0.2, callbacks=[early_stopping], verbose=1)

    # Evaluate the model on the test set
    loss, accuracy = model.evaluate(X_test, y_test)
    accuracy_percentage = accuracy * 100  # Convert to percentage
    error_rate = (1 - accuracy) * 100  # Convert to percentage
    print(f'Loss for {colName}: {loss:.4f}')
    print(f'Accuracy for {colName}: {accuracy_percentage:.2f}%')
    print(f'Error Rate for {colName}: {error_rate:.2f}%')

    # Predict on the entire dataset
    predictions = model.predict(features)
    predicted_classes = np.argmax(predictions, axis=1)  # Convert softmax outputs to class indices
    y_labels = np.argmax(y, axis=1)  # Convert one-hot encoded labels to class indices

    # Calculate accuracy
    accuracy = accuracy_score(y_labels, predicted_classes)
    accuracy_percentage_manual = accuracy * 100  # Convert to percentage
    error_rate_manual = (1 - accuracy) * 100  # Convert to percentage
    print(f'Accuracy (manual) for {colName}: {accuracy_percentage_manual:.2f}%')
    print(f'Error Rate (manual) for {colName}: {error_rate_manual:.2f}%')

    # Save the model
    model_file = os.path.join(model_dir, f'{colName}_softmax.h5')
    model.save(model_file)
    print(f'Model for {colName} saved to {model_file}')

    # Prepare data for impressions.csv
    impressions_data = []

    for i, (true_label, pred, predicted_class) in enumerate(zip(y_labels, predictions, predicted_classes)):
        row_data = {
            'DNo': data.iloc[i]['DNo'],
            'Location': data.iloc[i]['District'],
            'Social Category': data.iloc[i]['Social Category'],
            'Income': data.iloc[i]['Income'],
            'dropout': int(predicted_class)  # Add dropout column
        }
        if predicted_class == 1:  # Dropout
            row_data[f'{colName}_social_category'] = pred[0] * 100  # Convert to percentage
            row_data[f'{colName}_income'] = pred[1] * 100  # Convert to percentage
        else:  # Not dropout
            row_data[f'{colName}_social_category'] = 100 - (pred[1] * 100)  # Complementary percentage
            row_data[f'{colName}_income'] = 100 - (pred[0] * 100)  # Complementary percentage
        impressions_data.append(row_data)

    # Create DataFrame from the impressions data
    impressions_df = pd.DataFrame(impressions_data)

    # Save to CSV
    output_file = f'DATA/RNN Data/outputData/{colName}_impressions.csv'
    impressions_df.to_csv(output_file, index=False)

    return accuracy_percentage, impressions_df

# Create directory for models if it doesn't exist
model_dir = 'BackEnd//rnnModels//softmax//'
os.makedirs(model_dir, exist_ok=True)

# Load the data
try:
    data = pd.read_csv('DATA/RNN Data/final.csv')
except FileNotFoundError:
    raise FileNotFoundError("The data file was not found. Please check the file path.")

cols = ['prim_Girls', 'prim_Boys', 'prim_Overall', 'upPrim_Girls', 'upPrim_Boys', 'upPrim_Overall', 'snr_Girls', 'snr_Boys', 'snr_Overall']

# List to store DataFrames for each column and their accuracies
list_of_impressions = []
accuracies = {}

for colName in cols:
    # Modify data for each column
    data_copy = data.copy()
    data_copy[colName] = data_copy[colName].fillna(0)  # Fill NaN values as needed
    features, y, data_preprocessed = preprocess_data(data_copy, colName)
    accuracy, impressions_df = train_and_evaluate(features, y, data_preprocessed, colName, model_dir)
    list_of_impressions.append(impressions_df)
    accuracies[colName] = accuracy

# Find the best model based on accuracy
best_col = max(accuracies, key=accuracies.get)
best_accuracy = accuracies[best_col]
print(f'Best performing model is for column {best_col} with accuracy {best_accuracy:.2f}%')

# Concatenate all impressions dataframes
final_df = pd.concat(list_of_impressions, axis=1)

# Remove duplicate columns by keeping the first occurrence
final_df = final_df.loc[:, ~final_df.columns.duplicated()]

# Save the final concatenated dataframe
final_output_file = 'DATA/RNN Data/outputData/final_impressions.csv'
final_df.to_csv(final_output_file, index=False)

print(f"Final impressions data saved to {final_output_file}")
