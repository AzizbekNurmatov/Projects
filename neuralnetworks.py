# Import necessary libraries
import tkinter as tk  # For creating the graphical user interface
from tkinter import messagebox  # For displaying message boxes
import numpy as np  # For numerical operations on arrays
import tensorflow as tf  # For building and using the neural network
from tensorflow.keras.models import Sequential  # Sequential model structure
from tensorflow.keras.layers import Dense, Flatten  # Neural network layers
from tensorflow.keras.optimizers import Adam  # Optimizer for training the model
from tensorflow.keras.datasets import mnist  # MNIST dataset for training and testing
import cv2  # For image processing operations

# Function to load and preprocess the MNIST dataset
def load_and_preprocess_data():
    # Load MNIST dataset into training and testing sets
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    
    # Normalize the image data to range [0, 1] for faster training and better results
    x_train = x_train / 255.0
    x_test = x_test / 255.0
    
    # Return preprocessed data
    return (x_train, y_train), (x_test, y_test)

# Function to build the neural network model
def build_model():
    # Define a sequential model (stacked layers)
    model = Sequential([
        Flatten(input_shape=(28, 28)),  # Flatten 28x28 images into 1D vectors for the input layer
        Dense(128, activation='relu'),  # Hidden layer with 128 neurons and ReLU activation
        Dense(64, activation='relu'),  # Another hidden layer with 64 neurons and ReLU activation
        Dense(10, activation='softmax')  # Output layer with 10 neurons for digit classes (0-9)
    ]) #relu is rectified linear unit function or ramp function 
    
    # Compile the model with loss function, optimizer, and metrics
    model.compile(optimizer=Adam(learning_rate=0.001),  # Adam optimizer with learning rate 0.001 -> Adaptive Moment Estimation 
                  loss='sparse_categorical_crossentropy',  # Loss function for multi-class classification
                  metrics=['accuracy'])  # Metric to track during training
    return model

# Function to train the neural network model
def train_model():
    # Load preprocessed training and testing data
    (x_train, y_train), (x_test, y_test) = load_and_preprocess_data()
    
    # Build the model architecture
    model = build_model()
    
    # Train the model on the training data, validating on the test set
    model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test)) # epoch is number of passes
    
    # Save the trained model to a file for later use
    model.save("digit_recognizer.h5")
    return model

# Function to predict the digit based on the drawn image
def predict_digit(model, image):
    # Resize the input image to 28x28 pixels as required by the model
    image = cv2.resize(image, (28, 28))
    
    # Convert the resized image to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Normalize pixel values to the range [0, 1]
    image = image / 255.0
    
    # Add a batch dimension to the image to match the model's input shape
    image = np.expand_dims(image, axis=0)
    
    # Predict the digit using the trained model
    predictions = model.predict(image)
    
    # Return the index of the highest probability as the predicted digit
    return np.argmax(predictions)

# Class for the graphical application to draw digits and predict them
class DigitRecognizerApp:
    def __init__(self, root, model):
        self.root = root  # Tkinter root window
        self.model = model  # Trained neural network model
        
        # Create a canvas for drawing, with a white background
        self.canvas = tk.Canvas(root, width=280, height=280, bg="white")
        self.canvas.pack()  # Add the canvas to the window
        
        # Button to clear the canvas
        self.button_clear = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.button_clear.pack()  # Add the clear button below the canvas
        
        # Button to predict the digit drawn on the canvas
        self.button_predict = tk.Button(root, text="Predict", command=self.predict)
        self.button_predict.pack()  # Add the predict button below the clear button
        
        # Bind the mouse motion to the drawing function
        self.canvas.bind("<B1-Motion>", self.draw)
        
        # Create an image array to store the drawing as pixel data
        self.image = np.zeros((280, 280, 3), dtype=np.uint8)

    # Function to draw on the canvas
    def draw(self, event):
        x, y = event.x, event.y  # Get the current mouse coordinates
        r = 8  # Define the radius of the brush
        
        # Draw an oval (circle) at the current mouse position
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="black", outline="black")
        
        # Update the image array to reflect the drawing
        cv2.circle(self.image, (x, y), r, (255, 255, 255), -1)

    # Function to clear the canvas
    def clear_canvas(self):
        self.canvas.delete("all")  # Remove all drawings from the canvas
        self.image.fill(0)  # Reset the image array to all black

    # Function to predict the drawn digit
    def predict(self):
        digit = predict_digit(self.model, self.image)  # Predict the digit using the model
        # Show the predicted digit in a message box
        messagebox.showinfo("Prediction", f"The digit is: {digit}")

# Main function to run the application
if __name__ == "__main__":
    try:
        # Try loading a pre-trained model from file
        model = tf.keras.models.load_model("digit_recognizer.h5")
    except FileNotFoundError:
        # If the model file doesn't exist, train a new model
        model = train_model()

    # Create the Tkinter root window
    root = tk.Tk()
    root.title("Digit Recognizer")  # Set the window title
    
    # Create and run the digit recognizer application
    app = DigitRecognizerApp(root, model)
    