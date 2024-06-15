import json
def generate_plan_test():
    plan_json = {
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
                        },
                        {
                            "name": "Squats",
                            "description": "A basic squat exercise",
                            "image_url": "http://example.com/squats.jpg",
                            "video_url": "http://example.com/squats.mp4",
                            "reps": 20,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 150
                        },
                        {
                            "name": "Jumping Jacks",
                            "description": "A basic jumping jacks exercise",
                            "image_url": "http://example.com/jumpingjacks.jpg",
                            "video_url": "http://example.com/jumpingjacks.mp4",
                            "reps": 30,
                            "sets": 3,
                            "duration_minutes": 5,
                            "calories": 100
                        },
                        {
                            "name": "Plank",
                            "description": "A basic plank exercise",
                            "image_url": "http://example.com/plank.jpg",
                            "video_url": "http://example.com/plank.mp4",
                            "reps": 1,
                            "sets": 3,
                            "duration_minutes": 5,
                            "calories": 50
                        },
                        {
                            "name": "Running",
                            "description": "Running at a moderate pace",
                            "image_url": "http://example.com/running.jpg",
                            "video_url": "http://example.com/running.mp4",
                            "reps": 1,
                            "sets": 1,
                            "duration_minutes": 20,
                            "calories": 100
                        }
                    ],
                    "meal": [
                        {
                            "name": "Scrambled eggs with vegetables",
                            "description": "Breakfast",
                            "image_url": "http://example.com/breakfast.jpg",
                            "calories": 400,
                            "protein": 20,
                            "carbs": 30,
                            "fat": 15
                        },
                        {
                            "name": "Grilled chicken salad",
                            "description": "Lunch",
                            "image_url": "http://example.com/lunch.jpg",
                            "calories": 600,
                            "protein": 40,
                            "carbs": 50,
                            "fat": 20
                        },
                        {
                            "name": "Protein shake",
                            "description": "Snack",
                            "image_url": "http://example.com/snack.jpg",
                            "calories": 200,
                            "protein": 30,
                            "carbs": 10,
                            "fat": 5
                        },
                        {
                            "name": "Baked salmon with quinoa",
                            "description": "Dinner",
                            "image_url": "http://example.com/dinner.jpg",
                            "calories": 800,
                            "protein": 50,
                            "carbs": 60,
                            "fat": 30
                        }
                    ]
                },
                {
                    "name_day": "Day 2",
                    "description": "Workout and meals for day 2",
                    "calories_burned_per_day": 550,
                    "calories_intake_per_day": 2000,
                    "workout": [
                        {
                            "name": "Burpees",
                            "description": "A high-intensity full-body exercise",
                            "image_url": "http://example.com/burpees.jpg",
                            "video_url": "http://example.com/burpees.mp4",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 10,
                            "calories": 150
                        },
                        {
                            "name": "Lunges",
                            "description": "A basic lunge exercise",
                            "image_url": "http://example.com/lunges.jpg",
                            "video_url": "http://example.com/lunges.mp4",
                            "reps": 20,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 150
                        },
                        {
                            "name": "Mountain Climbers",
                            "description": "A basic mountain climber exercise",
                            "image_url": "http://example.com/mountainclimbers.jpg",
                            "video_url": "http://example.com/mountainclimbers.mp4",
                            "reps": 30,
                            "sets": 3,
                            "duration_minutes": 5,
                            "calories": 100
                        },
                        {
                            "name": "Bicycle Crunches",
                            "description": "A basic bicycle crunch exercise",
                            "image_url": "http://example.com/bicyclecrunches.jpg",
                            "video_url": "http://example.com/bicyclecrunches.mp4",
                            "reps": 20,
                            "sets": 3,
                            "duration_minutes": 10,
                            "calories": 100
                        },
                        {
                            "name": "Jump Rope",
                            "description": "Jumping rope for cardio",
                            "image_url": "http://example.com/jumprope.jpg",
                            "video_url": "http://example.com/jumprope.mp4",
                            "reps": 1,
                            "sets": 1,
                            "duration_minutes": 20,
                            "calories": 150
                        }
                    ],
                    "meal": [
                        {
                            "name": "Oatmeal with fruits",
                            "description": "Breakfast",
                            "image_url": "http://example.com/breakfast2.jpg",
                            "calories": 400,
                            "protein": 15,
                            "carbs": 70,
                            "fat": 10
                        },
                        {
                            "name": "Turkey sandwich with salad",
                            "description": "Lunch",
                            "image_url": "http://example.com/lunch2.jpg",
                            "calories": 600,
                            "protein": 35,
                            "carbs": 50,
                            "fat": 20
                        },
                        {
                            "name": "Greek yogurt with berries",
                            "description": "Snack",
                            "image_url": "http://example.com/snack2.jpg",
                            "calories": 200,
                            "protein": 15,
                            "carbs": 30,
                            "fat": 5
                        },
                        {
                            "name": "Stir-fried tofu with vegetables",
                            "description": "Dinner",
                            "image_url": "http://example.com/dinner2.jpg",
                            "calories": 800,
                            "protein": 40,
                            "carbs": 70,
                            "fat": 20
                        }
                    ]
                },
                {
                    "name_day": "Day 3",
                    "description": "Workout and meals for day 3",
                    "calories_burned_per_day": 600,
                    "calories_intake_per_day": 2000,
                    "workout": [
                        {
                            "name": "Deadlift",
                            "description": "A basic deadlift exercise",
                            "image_url": "http://example.com/deadlift.jpg",
                            "video_url": "http://example.com/deadlift.mp4",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 200
                        },
                        {
                            "name": "Bench Press",
                            "description": "A basic bench press exercise",
                            "image_url": "http://example.com/benchpress.jpg",
                            "video_url": "http://example.com/benchpress.mp4",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 150
                        },
                        {
                            "name": "Bent Over Row",
                            "description": "A basic bent over row exercise",
                            "image_url": "http://example.com/bentoverrow.jpg",
                            "video_url": "http://example.com/bentoverrow.mp4",
                            "reps": 20,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 150
                        },
                        {
                            "name": "Tricep Dips",
                            "description": "A basic tricep dips exercise",
                            "image_url": "http://example.com/tricepdips.jpg",
                            "video_url": "http://example.com/tricepdips.mp4",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 10,
                            "calories": 100
                        },
                        {
                            "name": "Running",
                            "description": "Running at a moderate pace",
                            "image_url": "http://example.com/running.jpg",
                            "video_url": "http://example.com/running.mp4",
                            "reps": 1,
                            "sets": 1,
                            "duration_minutes": 20,
                            "calories": 100
                        }
                    ],
                    "meal": [
                        {
                            "name": "Smoothie bowl",
                            "description": "Breakfast",
                            "image_url": "http://example.com/breakfast3.jpg",
                            "calories": 400,
                            "protein": 20,
                            "carbs": 50,
                            "fat": 10
                        },
                        {
                            "name": "Chicken and brown rice",
                            "description": "Lunch",
                            "image_url": "http://example.com/lunch3.jpg",
                            "calories": 600,
                            "protein": 40,
                            "carbs": 60,
                            "fat": 15
                        },
                        {
                            "name": "Protein bar",
                            "description": "Snack",
                            "image_url": "http://example.com/snack3.jpg",
                            "calories": 200,
                            "protein": 20,
                            "carbs": 20,
                            "fat": 5
                        },
                        {
                            "name": "Beef stir-fry with vegetables",
                            "description": "Dinner",
                            "image_url": "http://example.com/dinner3.jpg",
                            "calories": 800,
                            "protein": 50,
                            "carbs": 60,
                            "fat": 25
                        }
                    ]
                },
                {
                    "name_day": "Day 4",
                    "description": "Workout and meals for day 4",
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
                        },
                        {
                            "name": "Squats",
                            "description": "A basic squat exercise",
                            "image_url": "http://example.com/squats.jpg",
                            "video_url": "http://example.com/squats.mp4",
                            "reps": 20,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 150
                        },
                        {
                            "name": "Jumping Jacks",
                            "description": "A basic jumping jacks exercise",
                            "image_url": "http://example.com/jumpingjacks.jpg",
                            "video_url": "http://example.com/jumpingjacks.mp4",
                            "reps": 30,
                            "sets": 3,
                            "duration_minutes": 5,
                            "calories": 100
                        },
                        {
                            "name": "Plank",
                            "description": "A basic plank exercise",
                            "image_url": "http://example.com/plank.jpg",
                            "video_url": "http://example.com/plank.mp4",
                            "reps": 1,
                            "sets": 3,
                            "duration_minutes": 5,
                            "calories": 50
                        },
                        {
                            "name": "Running",
                            "description": "Running at a moderate pace",
                            "image_url": "http://example.com/running.jpg",
                            "video_url": "http://example.com/running.mp4",
                            "reps": 1,
                            "sets": 1,
                            "duration_minutes": 20,
                            "calories": 100
                        }
                    ],
                    "meal": [
                        {
                            "name": "Scrambled eggs with vegetables",
                            "description": "Breakfast",
                            "image_url": "http://example.com/breakfast.jpg",
                            "calories": 400,
                            "protein": 20,
                            "carbs": 30,
                            "fat": 15
                        },
                        {
                            "name": "Grilled chicken salad",
                            "description": "Lunch",
                            "image_url": "http://example.com/lunch.jpg",
                            "calories": 600,
                            "protein": 40,
                            "carbs": 50,
                            "fat": 20
                        },
                        {
                            "name": "Protein shake",
                            "description": "Snack",
                            "image_url": "http://example.com/snack.jpg",
                            "calories": 200,
                            "protein": 30,
                            "carbs": 10,
                            "fat": 5
                        },
                        {
                            "name": "Baked salmon with quinoa",
                            "description": "Dinner",
                            "image_url": "http://example.com/dinner.jpg",
                            "calories": 800,
                            "protein": 50,
                            "carbs": 60,
                            "fat": 30
                        }
                    ]
                },
                {
                    "name_day": "Day 5",
                    "description": "Workout and meals for day 5",
                    "calories_burned_per_day": 550,
                    "calories_intake_per_day": 2000,
                    "workout": [
                        {
                            "name": "Burpees",
                            "description": "A high-intensity full-body exercise",
                            "image_url": "http://example.com/burpees.jpg",
                            "video_url": "http://example.com/burpees.mp4",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 10,
                            "calories": 150
                        },
                        {
                            "name": "Lunges",
                            "description": "A basic lunge exercise",
                            "image_url": "http://example.com/lunges.jpg",
                            "video_url": "http://example.com/lunges.mp4",
                            "reps": 20,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 150
                        },
                        {
                            "name": "Mountain Climbers",
                            "description": "A basic mountain climber exercise",
                            "image_url": "http://example.com/mountainclimbers.jpg",
                            "video_url": "http://example.com/mountainclimbers.mp4",
                            "reps": 30,
                            "sets": 3,
                            "duration_minutes": 5,
                            "calories": 100
                        },
                        {
                            "name": "Bicycle Crunches",
                            "description": "A basic bicycle crunch exercise",
                            "image_url": "http://example.com/bicyclecrunches.jpg",
                            "video_url": "http://example.com/bicyclecrunches.mp4",
                            "reps": 20,
                            "sets": 3,
                            "duration_minutes": 10,
                            "calories": 100
                        },
                        {
                            "name": "Jump Rope",
                            "description": "Jumping rope for cardio",
                            "image_url": "http://example.com/jumprope.jpg",
                            "video_url": "http://example.com/jumprope.mp4",
                            "reps": 1,
                            "sets": 1,
                            "duration_minutes": 20,
                            "calories": 150
                        }
                    ],
                    "meal": [
                        {
                            "name": "Oatmeal with fruits",
                            "description": "Breakfast",
                            "image_url": "http://example.com/breakfast2.jpg",
                            "calories": 400,
                            "protein": 15,
                            "carbs": 70,
                            "fat": 10
                        },
                        {
                            "name": "Turkey sandwich with salad",
                            "description": "Lunch",
                            "image_url": "http://example.com/lunch2.jpg",
                            "calories": 600,
                            "protein": 35,
                            "carbs": 50,
                            "fat": 20
                        },
                        {
                            "name": "Greek yogurt with berries",
                            "description": "Snack",
                            "image_url": "http://example.com/snack2.jpg",
                            "calories": 200,
                            "protein": 15,
                            "carbs": 30,
                            "fat": 5
                        },
                        {
                            "name": "Stir-fried tofu with vegetables",
                            "description": "Dinner",
                            "image_url": "http://example.com/dinner2.jpg",
                            "calories": 800,
                            "protein": 40,
                            "carbs": 70,
                            "fat": 20
                        }
                    ]
                },
                {
                    "name_day": "Day 6",
                    "description": "Workout and meals for day 6",
                    "calories_burned_per_day": 600,
                    "calories_intake_per_day": 2000,
                    "workout": [
                        {
                            "name": "Deadlift",
                            "description": "A basic deadlift exercise",
                            "image_url": "http://example.com/deadlift.jpg",
                            "video_url": "http://example.com/deadlift.mp4",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 200
                        },
                        {
                            "name": "Bench Press",
                            "description": "A basic bench press exercise",
                            "image_url": "http://example.com/benchpress.jpg",
                            "video_url": "http://example.com/benchpress.mp4",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 150
                        },
                        {
                            "name": "Bent Over Row",
                            "description": "A basic bent over row exercise",
                            "image_url": "http://example.com/bentoverrow.jpg",
                            "video_url": "http://example.com/bentoverrow.mp4",
                            "reps": 20,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 150
                        },
                        {
                            "name": "Tricep Dips",
                            "description": "A basic tricep dips exercise",
                            "image_url": "http://example.com/tricepdips.jpg",
                            "video_url": "http://example.com/tricepdips.mp4",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 10,
                            "calories": 100
                        },
                        {
                            "name": "Running",
                            "description": "Running at a moderate pace",
                            "image_url": "http://example.com/running.jpg",
                            "video_url": "http://example.com/running.mp4",
                            "reps": 1,
                            "sets": 1,
                            "duration_minutes": 20,
                            "calories": 100
                        }
                    ],
                    "meal": [
                        {
                            "name": "Smoothie bowl",
                            "description": "Breakfast",
                            "image_url": "http://example.com/breakfast3.jpg",
                            "calories": 400,
                            "protein": 20,
                            "carbs": 50,
                            "fat": 10
                        },
                        {
                            "name": "Chicken and brown rice",
                            "description": "Lunch",
                            "image_url": "http://example.com/lunch3.jpg",
                            "calories": 600,
                            "protein": 40,
                            "carbs": 60,
                            "fat": 15
                        },
                        {
                            "name": "Protein bar",
                            "description": "Snack",
                            "image_url": "http://example.com/snack3.jpg",
                            "calories": 200,
                            "protein": 20,
                            "carbs": 20,
                            "fat": 5
                        },
                        {
                            "name": "Beef stir-fry with vegetables",
                            "description": "Dinner",
                            "image_url": "http://example.com/dinner3.jpg",
                            "calories": 800,
                            "protein": 50,
                            "carbs": 60,
                            "fat": 25
                        }
                    ]
                },
                {
                    "name_day": "Day 7",
                    "description": "Workout and meals for day 7",
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
                        },
                        {
                            "name": "Squats",
                            "description": "A basic squat exercise",
                            "image_url": "http://example.com/squats.jpg",
                            "video_url": "http://example.com/squats.mp4",
                            "reps": 20,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 150
                        },
                        {
                            "name": "Jumping Jacks",
                            "description": "A basic jumping jacks exercise",
                            "image_url": "http://example.com/jumpingjacks.jpg",
                            "video_url": "http://example.com/jumpingjacks.mp4",
                            "reps": 30,
                            "sets": 3,
                            "duration_minutes": 5,
                            "calories": 100
                        },
                        {
                            "name": "Plank",
                            "description": "A basic plank exercise",
                            "image_url": "http://example.com/plank.jpg",
                            "video_url": "http://example.com/plank.mp4",
                            "reps": 1,
                            "sets": 3,
                            "duration_minutes": 5,
                            "calories": 50
                        },
                        {
                            "name": "Running",
                            "description": "Running at a moderate pace",
                            "image_url": "http://example.com/running.jpg",
                            "video_url": "http://example.com/running.mp4",
                            "reps": 1,
                            "sets": 1,
                            "duration_minutes": 20,
                            "calories": 100
                        }
                    ],
                    "meal": [
                        {
                            "name": "Scrambled eggs with vegetables",
                            "description": "Breakfast",
                            "image_url": "http://example.com/breakfast.jpg",
                            "calories": 400,
                            "protein": 20,
                            "carbs": 30,
                            "fat": 15
                        },
                        {
                            "name": "Grilled chicken salad",
                            "description": "Lunch",
                            "image_url": "http://example.com/lunch.jpg",
                            "calories": 600,
                            "protein": 40,
                            "carbs": 50,
                            "fat": 20
                        },
                        {
                            "name": "Protein shake",
                            "description": "Snack",
                            "image_url": "http://example.com/snack.jpg",
                            "calories": 200,
                            "protein": 30,
                            "carbs": 10,
                            "fat": 5
                        },
                        {
                            "name": "Baked salmon with quinoa",
                            "description": "Dinner",
                            "image_url": "http://example.com/dinner.jpg",
                            "calories": 800,
                            "protein": 50,
                            "carbs": 60,
                            "fat": 30
                        }
                    ]
                }
            ]
        }
    print(f"Type: {type(plan_json)}")
    plan1 = json.dumps(plan_json)
    plan = json.loads(plan1)
    print(f"Type: {type(plan)}")
    return plan
