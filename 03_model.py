import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Path to the model
model_path = r"C:/Users/USER/OneDrive/Desktop/Image-Classification-Project/Image-Classification-Model-for-Wheat-Crop-Disease-1/Model/wheat_disease_classification_model.h5"

# Load the model
model = load_model(model_path)

# Custom CSS for styling the app
st.markdown("""
    <style>
    .main {
        background-color: #8a7c12;
        color: #dadbe6;
    }
    .title {
        color: #09090a;
        font-size: 34px;
        text-align: center;
        font-weight: bold;
        padding-bottom: 10px;
    }
    .upload-container {
        display: flex;
        justify-content: center;
        padding: 20px;
        margin-top: 30px;
    }
    .upload-button {
        background-color: #e74c3c;
        color: white;
        padding: 10px 25px;
        border-radius: 5px;
        font-size: 14px;
        cursor: pointer;
        border: none;
    }
    .upload-button:hover {
        background-color: #c0392b;
    }
    .prediction-container {
        margin-top: 20px;
        padding: 15px;
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
    }
    .prediction-title {
        font-size: 20px;
        font-weight: bold;
        color: #2c3e50;
    }
    .prediction-result {
        font-size: 16px;
        color: #16a085;
    }
    .image-container {
        display: flex;
        justify-content: center;
        padding-top: 15px;
    }
    .footer {
        font-size: 12px;
        text-align: center;
        color: #95a5a6;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">Wheat Pest and Disease Identifier</p>', unsafe_allow_html=True)

# Description
st.write("Upload a photo of your wheat crop, and this app will classify the image to detect possible pests or diseases.")

# File uploader for images
st.markdown('<div class="upload-container">', unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "Select an image file...", 
    type=["jpg", "jpeg", "png"], 
    key="image_uploader", 
    label_visibility="collapsed"
)
st.markdown('</div>', unsafe_allow_html=True)

# Image preprocessing function
def preprocess_image(img):
    img = image.load_img(img, target_size=(224, 224))  # Resize image
    img_array = image.img_to_array(img) / 255.0  # Normalize pixel values
    return np.expand_dims(img_array, axis=0)  # Add batch dimension

# Display results if an image is uploaded
if uploaded_file is not None:
    img = preprocess_image(uploaded_file)
    
    # Model prediction
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction, axis=1)

    # Class-to-disease mapping
    class_names = [
        "Aphid", "Black Rust", "Blast", "Brown Rust", 
        "Common Root Rot", "Fusarium Head Blight", "Healthy", 
        "Leaf Blight", "Mildew", "Mite", "Septoria", 
        "Smut", "Stem Fly", "Tan Spot", "Yellow Rust"
    ]
    predicted_disease = class_names[predicted_class[0]]
    
    # Display the uploaded image
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Display prediction result
    st.markdown('<div class="prediction-container">', unsafe_allow_html=True)
    st.markdown(f'<p class="prediction-title">Diagnosis Result:</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="prediction-result">{predicted_disease}</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<p class="footer">Powered by AI | Wheat Health Assistant</p>', unsafe_allow_html=True)
