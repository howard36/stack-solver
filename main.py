from stackapi import StackAPI
from stackapi import StackAPIError
from dotenv import load_dotenv
from chatbot import Chatbot
import json
import os


with open("config.json", "r") as f:
    config = json.load(f)
chatbot = Chatbot(config)
if 'session_token' in config:
    chatbot.refresh_session()


load_dotenv()
key = os.getenv('KEY')
access_token = os.getenv('ACCESS_TOKEN')
site = StackAPI('stackoverflow', key=key, access_token=access_token, max_pages=1, page_size=1)

filter = 'aW)UqV5WKko7oxUpYV'

questions = site.fetch('questions/no-answers', tagged='math', sort='votes', filter=filter)


with open("prompt.txt", "r") as f:
    prompt_prefix = f.read()

with open("reply_suffix.txt", "r") as f:
    reply_suffix = f.read()


for question in questions['items']:
    prompt = prompt_prefix + question['body_markdown']
    print(message)
    try:
        response = chatbot.get_chat_response(message)
    except Exception as e:
        print(e)
        continue

    print("ChatGPT Response:")
    reply = response['message']
    print(response['message'])


