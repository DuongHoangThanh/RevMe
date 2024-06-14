import openai
import json
from dotenv import load_dotenv
import os

def generate_plan(goal_data, user_data):
    prompt = f"Generate a workout and diet plan based on the following goal data: {json.dumps(goal_data)}, returns JSON format"

    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )

    # Get the message from the response
    message = response['choices'][0]['message']['content']
    
    # option 1: return message
    # return message
    
    # option 2: return JSON object
    try:
        message_json = json.loads(message)
    except json.JSONDecodeError:
        print(f"Warning: Could not decode message into JSON: {message}")
        message_json = None

    return message_json