import streamlit as st

def show():
    st.title("Welcome to the Wheat disease classification Prediction application")

    container = st.container()
    col1, col2 = container.columns([5, 1])

    # Documentation and Details about the Application
    with col1:
        with st.expander("### About the Application", expanded=False):
            st.markdown("####  Wheat disease classification")
            st.write("""
                The Wheat disease classification prediction model is to be used to classify images of wheat crop pests and diseases to aid smallholder farmers in diagnosis.
            """)

            st.markdown("#### Key Features")
            st.write("""
                - **View Data**: Accessed data remotely downloaded from kaggle.
                - **Home**: Contains data visualizations to explore trends.
                - **Model**: Make real-time predictions with machine learning models.
            """)

            st.markdown("#### User Benefits")
            st.write("""
                - Make data-driven decisions effortlessly.
                - Harness the power of machine learning without the complexity.
                - Save and analyze your data securely.
            """)

            st.markdown("#### Machine Learning Integration")
            st.write("""
                The application allows you to incorporate transfer learning predictive model, providing flexibility and accuracy in forecasts.
            """)

            st.markdown("#### Documentation")
            st.write("""
                - [Source Code](https://github.com/raymondmusyoka/Image-Classification-Model-for-Wheat-Crop-Disease.git)
                - [Model Training](https://github.com/raymondmusyoka/Image-Classification-Model-for-Wheat-Crop-Disease.git)
            """)
        
        st.image("C:/Users/USER/OneDrive/Desktop/Image-Classification-Project/Image-Classification-Model-for-Wheat-Crop-Disease-1/Images/Wheat_image.jpeg", use_column_width="always")

    with col2:
        st.markdown("#### 🔗 Quick Links")
        st.write("""
            - [GitHub Repository](https://github.com/raymondmusyoka/Image-Classification-Model-for-Wheat-Crop-Disease.git)
            - [LinkedIn Profile](inkedin.com/in/raymond-musyoka/)
            - [Read on Medium](https://medium.com/@raymondmutati)
        """)

        st.markdown("##### 🤝 Connect with Me")
        st.write("""
            - [GitHub](https://github.com/raymondmusyoka)
            - [LinkedIn](inkedin.com/in/raymond-musyoka/)
            - [Medium](https://medium.com/@raymondmutati)
            - Contact me at [Email](raymutati@gmail.com)
        """)


if __name__ == "__main__":
    show()