import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import tensorflow as tf

def impression(data: pd.DataFrame, colName: str):
    # One-hot encode categorical columns
    encoder = OneHotEncoder(sparse=False, drop='first')  # Drop first to avoid multicollinearity
    categorical_cols = ['Social Category', 'Income']
    encoded_categorical = encoder.fit_transform(data[categorical_cols])

    # Normalize numerical columns
    scaler = MinMaxScaler()
    # numerical_cols = ['prim_Girls', 'prim_Boys', 'prim_Overall', 'upPrim_Girls', 'upPrim_Boys', 'upPrim_Overall', 'snr_Girls', 'snr_Boys', 'snr_Overall']
    normalized_numerical = scaler.fit_transform(data[colName].values.reshape(-1, 1))

    # Combine all features
    features = np.hstack([encoded_categorical, normalized_numerical])

    # Create target column for dropout (one-hot encoding)
    data['dropout'] = (data[colName] > 0).astype(int)
    y = pd.get_dummies(data['dropout']).values  # Convert to one-hot encoded format

    # Split data into features and target
    X = features

    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define RNN model
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(X_train.shape[1],)),
        tf.keras.layers.Reshape((X_train.shape[1], 1)),  # Reshape for RNN input
        tf.keras.layers.SimpleRNN(50, activation='relu'),
        tf.keras.layers.Dense(2, activation='softmax')  # Output layer with softmax for binary classification
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    history = model.fit(X_train, y_train, epochs=60, batch_size=32, validation_split=0.2)

    # Evaluate the model
    loss, accuracy = model.evaluate(X_test, y_test)
    accuracy_percentage = accuracy * 100  # Convert to percentage
    error_rate = (1 - accuracy) * 100  # Convert to percentage
    print(f'Loss: {loss:.4f}')
    print(f'Accuracy: {accuracy_percentage:.2f}%')
    print(f'Error Rate: {error_rate:.2f}%')

    # Predict on test set
    predictions = model.predict(X_test)
    predicted_classes = np.argmax(predictions, axis=1)  # Convert softmax outputs to class indices
    y_test_labels = np.argmax(y_test, axis=1)  # Convert one-hot encoded test labels to class indices

    # Calculate accuracy
    accuracy = accuracy_score(y_test_labels, predicted_classes)
    accuracy_percentage_manual = accuracy * 100  # Convert to percentage
    error_rate_manual = (1 - accuracy) * 100  # Convert to percentage
    print(f'Accuracy (manual): {accuracy_percentage_manual:.2f}%')
    print(f'Error Rate (manual): {error_rate_manual:.2f}%')

    # Prepare data for impressions.csv
    impressions_data = []

    for i, (true_label, pred, predicted_class) in enumerate(zip(y_test_labels, predictions, predicted_classes)):
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
    output_file = f'DATA\\RNN Data\\outputData\\{colName}_impressions.csv'
    impressions_df.to_csv(output_file, index=False)

    print(f"\nImpressions for {colName} (Probability Distributions as Percentages for Dropouts):")
    print(impressions_df)

    return impressions_df

# Load the data
data = pd.read_csv('DATA\\RNN Data\\final.csv')
cols = ['prim_Girls', 'prim_Boys', 'prim_Overall', 'upPrim_Girls', 'upPrim_Boys', 'upPrim_Overall', 'snr_Girls', 'snr_Boys', 'snr_Overall']

# List to store DataFrames for each column
list_of_impressions = []

for colName in cols:
    # Modify data for each column
    data_copy = data.copy()
    data_copy[colName] = data_copy[colName].fillna(0)  # Fill NaN values as needed, adjust if needed
    impressions_df = impression(data_copy, colName)
    list_of_impressions.append(impressions_df)

# Concatenate all impressions dataframes
final_df = pd.concat(list_of_impressions, axis=1)

# Remove duplicate columns by keeping the first occurrence
final_df = final_df.loc[:, ~final_df.columns.duplicated()]

# Save the final concatenated dataframe
final_df.to_csv('DATA\\RNN Data\\outputData\\final_impressions.csv', index=False)
