import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


def impression(data: pd.DataFrame, colName: str):
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
    history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

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

    # Prepare data for impressions.csv (only for dropouts)
    impressions_data = []

    for i, (true_label, pred, predicted_class) in enumerate(zip(y_test_labels, predictions, predicted_classes)):
        if predicted_class == 1:  # Only include dropout predictions
            pred_percentages = pred * 100  # Convert probabilities to percentages
            dno = data.iloc[i]['DNo']
            location = data.iloc[i]['District']
            caste = data.iloc[i]['Social Category']
            income = data.iloc[i]['Income']
            impressions_data.append([dno, location, caste, income, pred_percentages[0], pred_percentages[1]])

    impressions_df = pd.DataFrame(impressions_data, columns=['DNo', 'Location', 'Social Category', 'Income', f'{colName}_socialcat', f'{colName}_income'])
    impressions_df.to_csv(f'DATA\\RNN Data\\outputData\\{colName}impressions.csv', index=False)

    print("\nImpressions (Probability Distributions as Percentages for Dropouts):")
    print(impressions_df)

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

    return impressions_df

data = pd.read_csv('DATA\\RNN Data\\final.csv')
cols = ['prim_Girls', 'prim_Boys', 'prim_Overall', 'upPrim_Girls', 'upPrim_Boys', 'upPrim_Overall', 'snr_Girls', 'snr_Boys', 'snr_Overall']


list_of_impressions = []

for colName in cols:
    # impression(data, colName)
    list_of_impressions.append(impression(data, colName))
    
final_df = pd.concat(list_of_impressions, axis=1)

# print(final_df.head())
final_df = final_df.loc[:, ~final_df.columns.duplicated()]

final_df.to_csv('DATA\\RNN Data\\outputData\\final_impressions.csv', index=False)
    