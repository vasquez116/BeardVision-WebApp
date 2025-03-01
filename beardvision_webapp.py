import streamlit as st
import requests
import base64

# Backend API URL
API_URL = "https://your-backend-api-url/analyze_beard/"  # Replace with deployed API endpoint

# Streamlit UI
def main():
    st.title("🧔 BeardVision AI")
    st.write("Upload your image to get an AI-powered beard analysis!")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        
        # Convert image to base64
        image_bytes = uploaded_file.read()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        
        if st.button("Analyze Beard 🧐"):
            with st.spinner("Analyzing your beard..."):
                response = requests.post(API_URL, files={"file": image_bytes})
                
                if response.status_code == 200:
                    result = response.json()
                    if "error" in result:
                        st.error(result["error"])
                    else:
                        st.success("Analysis Complete!")
                        st.write("### Beard Features:")
                        st.json(result["features"])
                else:
                    st.error("Failed to process image. Try again later.")

if __name__ == "__main__":
    main()
