import streamlit as st
import openai
from dotenv import load_dotenv
import os
# Set up OpenAI API
# Load the .env file
load_dotenv()

# Fetch the API key from the environment
openai.api_key =st.secrets["api_key"]


# Streamlit app title
st.title('Comprehensive Carbon Emission Rate Checker')

# Select category
category = st.selectbox("Select the item category:", ["Food", "Fuel", "Electricity", "Other"])

# Input from the user based on category
if category == "Food":
    item = st.text_input("Enter the food item (e.g., Chapati):")
elif category == "Fuel":
    item = st.text_input("Enter the fuel type and quantity (e.g., 2 liters of Petrol):")
elif category == "Electricity":
    item = st.text_input("Enter electricity usage in kWh (e.g., 100 kWh):")
else:
    item = st.text_input("Enter the item for carbon emission calculation:")

if st.button("Calculate Emission"):
    # Define a dynamic prompt based on user input
    prompt = (f"Provide a detailed explanation including emission rate values and a clear breakdown for the carbon emission of {item}. "
              "Use HTML formatting to highlight each heading in black color, like <h2 style='color:black;'>Heading</h2>. "
              "Make sure to include the emissions breakdown clearly.")

    # Get the response from OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant for calculating carbon emissions."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500  # Increase token limit for detailed responses
    )

    # Display the result with HTML formatting for headings
    emission_details = response['choices'][0]['message']['content'].strip()
    st.write(f"Carbon Emission Details for {item}:")
    st.markdown(emission_details, unsafe_allow_html=True)  # Render HTML content
