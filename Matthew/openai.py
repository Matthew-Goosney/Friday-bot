from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('API_KEY')

def chat_gpt_response(prompt)
    response = openai.Completion.create(
        

    )