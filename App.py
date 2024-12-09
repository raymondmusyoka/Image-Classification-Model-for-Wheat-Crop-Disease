# Import necessary libraries
import streamlit as st
import os

# Configure the page
st.set_page_config(
    page_title='Wheat Pest Classification App',
    page_icon='🌾',
    layout='wide',
    initial_sidebar_state='auto'
)

# Add custom CSS to adjust the width of the sidebar
st.markdown("""
    <style> 
        section[data-testid="stSidebar"] {
            width: 200px !important;
        }
    </style> 
""", unsafe_allow_html=True)

def main():
    st.header('Wheat Pest Classification App')

    st.write(
        """
        Welcome to the **Wheat Pest Classification App**! This app is designed to assist smallholder farmers and agricultural professionals in diagnosing wheat pests and diseases using advanced image classification techniques.
        """
    )

    cols = st.columns(2)

    # About the App
    with cols[0]:
        st.subheader('About the App')
        st.write(
            """
            This application leverages advanced convolutional neural networks (CNNs) to classify images of wheat crops, identifying pests and diseases accurately. The app aims to:
            
            * Help farmers identify pests and diseases early
            * Provide actionable insights for managing crop health
            * Support sustainable and efficient farming practices
            
            With its easy-to-use interface and robust classification models, this app empowers users to enhance crop yield and quality.
            """
        )

    # Application Features
    with cols[0]:
        st.subheader('Key Features')
        st.markdown("""
            * **Data View**: Explore and analyze image data of wheat crops to understand pest and disease distributions.
            * **Dashboard**: Visualize key metrics such as pest prevalence, disease trends, and affected regions through interactive charts and graphs.
            * **Predict**: Use our image classification model to diagnose wheat pests and diseases based on uploaded images.
            * **History**: Review past predictions and monitor trends to support proactive pest and disease management.
            """)

    # Key Advantages
    with cols[0]:
        st.subheader('Why Use This App?')
        st.markdown("""
            * **Accurate Predictions**: Utilize advanced machine learning models for precise identification of wheat pests and diseases.
            * **Intuitive Interface**: Experience a user-friendly interface designed for farmers and agricultural professionals.
            * **Actionable Insights**: Gain valuable insights into pest and disease patterns to inform effective management strategies.
            * **Continuous Improvement**: Benefit from regular updates and enhancements, ensuring the model stays up-to-date with the latest agricultural research.
            """)

    # How to Run the App
    with cols[1]:
        st.subheader('How to Get Started')
        st.write("Follow these steps to run the Wheat Pest Classification App:")
        st.code("""
            # Activate your virtual environment
            venv/Scripts/activate

            # Run the Streamlit app
            streamlit run app.py
            """, language="python")

    # Machine Learning Integration
    with cols[1]:
        st.subheader('Machine Learning Models')
        st.write(
            """
            Our app integrates advanced convolutional neural networks (CNNs) to classify wheat crop images. These models are trained on a diverse dataset to deliver accurate and reliable pest and disease diagnoses.
            """
        )

    # Need Assistance
    with cols[1]:
        st.subheader('Need Help?')
        st.write(
            """
            If you encounter any issues or have questions, please don't hesitate to reach out:
            - **Email**: raymutati@gmail.com
            - **GitHub**: [GitHub Repository](https://github.com/raymondmusyoka/Image-Classification-Model-for-Wheat-Crop-Disease.git)
            - **LinkedIn**: [Connect on LinkedIn](http://www.linkedin.com/in/raymond-musyoka/)
            """
        )

if __name__ == '__main__':
    main()
