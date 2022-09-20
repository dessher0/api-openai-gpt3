import os
from dotenv import load_dotenv
from flask import Flask, request
import openai

load_dotenv()

openai.api_key = os.getenv('API_KEY')
completion = openai.Completion()

start_sequence = "\nYou:"
restart_sequence = "\n\nAI:"
session_prompt = "This is a conversation with an AI assistant."

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}'
    response = completion.create(
        engine="text-davinci-002",
        prompt=prompt_text,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    return str(response['choices'][0]['text'])

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{start_sequence} {question}{restart_sequence}{answer}'