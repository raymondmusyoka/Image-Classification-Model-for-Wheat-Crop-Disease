import os
import streamlit as st

# Load Data
@st.cache_data(persist=True)
def load_data():
    # Initialize the path to the original input directory of images
    data_dir = "C:/Users/USER/OneDrive/Desktop/Image-Classification-Project/Notebooks"

    # Derive the training, validation, and testing directories
    test_path = os.path.join(data_dir, 'test')
    train_path = os.path.join(data_dir, 'train')
    valid_path = os.path.join(data_dir, 'valid')

    # Return directory paths and their file listings
    return {
        "data_dir": os.listdir(data_dir),
        "test_dir": os.listdir(test_path) if os.path.exists(test_path) else "Path not found",
        "train_dir": os.listdir(train_path) if os.path.exists(train_path) else "Path not found",
        "valid_dir": os.listdir(valid_path) if os.path.exists(valid_path) else "Path not found",
    }

# Display the directories and their contents in Streamlit
data = load_data()

st.write("## Directory Overview")
st.write(f"**Data Directory:** {data['data_dir']}")
st.write(f"**Test Directory:** {data['test_dir']}")
st.write(f"**Train Directory:** {data['train_dir']}")
st.write(f"**Validation Directory:** {data['valid_dir']}")

