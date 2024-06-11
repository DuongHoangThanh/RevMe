from openai import OpenAI

openai = OpenAI()

import json
client = OpenAI()

prompt = "G eneratse a workout plan for a male who is 50 years old and has a Beginner fitnes level. They want to target Full Body and have a 30-minute workout.!"
json_format = {
    "workout_plan": {
        "target": "Full Body",
        "duration": "15 minutes",
        "exercises": [
            {"name": "Push-ups", "description": "Stand with feet shoulder-width apart, lower your body by bending your knees, then return to starting position.", "sets": 3, "reps": 10},
        ]     
    }
}
chat_response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Provide output in valid JSON format., The data scheme should be like this: " + json.dumps(json_format)},
        {"role": "system", "content": "The response should be no more than 250 characters long."},
        {"role": "system", "content": "You are a fitness trainer."},
        {"role": "user", "content": prompt},
    ],
    # max_tokens=200,
    response_format={"type": "json_object"}
)

data = chat_response.choices[0].message.content

print(json.loads(data))
