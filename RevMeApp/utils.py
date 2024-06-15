import openai
import json
from dotenv import load_dotenv
import os

def generate_plan(goal_data, user_data):
    prompt = f"""
        Create a 7-day workout and meal plan in JSON format based on the following user data, goal:
        User data: Age:{user_data.age}, Gender:{user_data.gender}, Weight:{user_data.weight}kg, Height:{user_data.height}m, Condition: {user_data.NObeyesdad}
        Goal: Type: {goal_data.goal_type}, Target Weight:{goal_data.target_weight_kg}kg, Duration: {goal_data.duration_weeks}weeks
        """+ """
        The plan should include the following details for each day:

        1. **Name of the day**: A string representing the day of the plan (e.g., "Day 1").
        2. **Description**: A string describing the activities and meals of the day.
        3. **Calories burned per day**: An integer representing the total calories burned from workouts.
        4. **Calories intake per day**: An integer representing the total calories consumed from meals.
        5. **Workout**: A list of exercises, where each exercise includes:
        - **Name**: The name of the exercise (e.g., "Push-up").
        - **Description**: A brief description of the exercise.
        - **Image URL**: A URL link to an image demonstrating the exercise.
        - **Video URL**: A URL link to a video demonstrating the exercise.
        - **Reps**: The number of repetitions for the exercise.
        - **Sets**: The number of sets for the exercise.
        - **Duration minutes**: The duration of the exercise in minutes.
        - **Calories**: The number of calories burned by performing the exercise.
        6. **Meal**: A list of meals, where each meal includes:
        - **Name**: The name of the meal (e.g., "Breakfast").
        - **Description**: A brief description of the meal.
        - **Image URL**: A URL link to an image of the meal.
        - **Calories**: The number of calories in the meal.
        - **Protein**: The amount of protein in grams.
        - **Carbs**: The amount of carbohydrates in grams.
        - **Fat**: The amount of fat in grams.

        Here is an example of the JSON format:

        {
            "plan": [
                {
                    "name_day": "Day 1",
                    "description": "Workout and meals for day 1",
                    "calories_burned_per_day": 500,
                    "calories_intake_per_day": 2000,
                    "workout": [
                        {
                            "name": "Push-up",
                            "description": "A basic push-up exercise",
                            "image_url": "http://example.com/pushup.jpg",
                            "video_url": "http://example.com/pushup.mp4",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 10,
                            "calories": 100
                        }
                    ],
                    "meal": [
                        {
                            "name": "Scrambled eggs with vegetables",
                            "description": "Breakfast",
                            "image_url": "http://example.com/breakfast.jpg",
                            "calories": 500,
                            "protein": 20,
                            "carbs": 50,
                            "fat": 10
                        }
                    ]
                }
            ]
        }
        Generate a similar plan for the next 6 days.
        """
        
    load_dotenv()
    openai.api_key = os.getenv("openai_key")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        temperature=1,
        # max_tokens=16384,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0, 
        # response_format={"type": "json_object"}
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