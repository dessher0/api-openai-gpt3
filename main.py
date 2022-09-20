import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv('MY_API_KEY')


response = openai.Completion.create(
    engine="text-davinci-002",
    max_tokens=256,
    prompt=input("Enter your prompt: "),
    temperature=0.7,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

print('Response: {0}'.format(response['choices'][0]['text']))