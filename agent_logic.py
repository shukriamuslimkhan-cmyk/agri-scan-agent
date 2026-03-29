import os
from groq import Groq  # Changed import
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq Client instead of OpenAI
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def get_treatment_plan(disease_name, confidence):
    # Use Llama 3 model (Fast & Free)
    model = "llama3-8b-8192" 
    
    prompt = f"""
    You are an expert agronomist. 
    Detected Disease: {disease_name}
    Confidence Score: {confidence}%
    
    Task: 
    1. Confirm the diagnosis briefly.
    2. Provide 3 actionable treatment steps (1 Organic, 1 Chemical, 1 Preventive).
    3. Keep the tone encouraging for farmers.
    """

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=500
    )
    
    return response.choices[0].message.content