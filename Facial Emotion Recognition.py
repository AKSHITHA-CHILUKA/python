# Import Libraries
import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split

# Load the Dataset
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    emotions = []
    pixels = []
    
    for index, row in data.iterrows():
        emotion = row['emotion']
        img = np.fromstring(row['pixels'], sep=' ').reshape(48, 48)
        emotions.append(emotion)
        pixels.append(img)
    
    X = np.array(pixels)
    y = np.array(emotions)
    return X, y

# Preprocess the Data
def preprocess_data(X, y):
    X = X.astype('float32') / 255.0  # Normalize pixel values
    X = np.expand_dims(X, axis=-1)    # Add channel dimension
    y = to_categorical(y, num_classes=7)  # One-hot encode labels
    return X, y

# Load and Preprocess the Dataset
X, y = load_data('fer2013.csv')  # Adjust the path to your dataset
X, y = preprocess_data(X, y)

# Split the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the CNN Model
def create_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(48, 48, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(7, activation='softmax'))  # 7 classes for emotions
    return model

# Compile the Model
model = create_model()
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the Model
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

# Evaluate the Model
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f'Test accuracy: {test_accuracy:.2f}')

# Predict Emotion Function
def predict_emotion(image):
    processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.resize(processed_image, (48, 48))
    processed_image = processed_image.astype('float32') / 255.0
    processed_image = np.expand_dims(processed_image, axis=0)
    processed_image = np.expand_dims(processed_image, axis=-1)
    prediction = model.predict(processed_image)
    emotion = np.argmax(prediction)
    return emotion

# Example Usage
if __name__ == '__main__':
    # Load an example image
    image_path = 'example.jpg'  # Replace with your image path
    image = cv2.imread(image_path)
    
    # Predict Emotion
    emotion = predict_emotion(image)
    print(f'Predicted Emotion: {emotion}')  # 0-6 for different emotions
