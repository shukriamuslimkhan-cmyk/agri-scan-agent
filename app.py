import streamlit as st
from src.model_loader import load_model
from PIL import Image

st.set_page_config(page_title="Agri-Scan Agent", layout="wide")
st.title("🌱 Agri-Scan: Autonomous Crop Doctor")

model = load_model()

uploaded_file = st.file_uploader("Upload Leaf Image", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Leaf", use_column_width=True)
    
    if st.button("Analyze Health"):
        with st.spinner("AI Agent is diagnosing..."):
            # Run Inference
            results = model.predict(image, conf=0.5)
            # Display Results (Plot or Boxes)
            st.write("Detection Complete.")
            
# Inside the button click logic
#with st.spinner("🤖 Groq AI Agent is analyzing..."):
    #treatment = get_treatment_plan(class_name, confidence_score)
    #st.success(treatment)