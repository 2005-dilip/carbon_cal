from dotenv import load_dotenv
import os
import openai

# Load the .env file
load_dotenv()

# Fetch the API key from the environment
openai.api_key = os.getenv('OPENAI_API_KEY')

# Test by printing the API key (remove this line later for security)
print(openai.api_key)

# Rest of your code...
