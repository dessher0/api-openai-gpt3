import openai
import config


openai.api_key = config.OPENAI_API_KEY

def main():
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=input("Enter your prompt: "),
    temperature=0.3,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    )

    return response['choices'][0]['text']