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
                            "image_url": "https://media.self.com/photos/57d889aef71ce8751f6b48f8/4:3/w_2560%2Cc_limit/push-up-tips_Feat.jpg",
                            "video_url": "https://www.youtube.com/watch?v=IODxDxX7oi4&pp=ygUHUHVzaC11cA%3D%3D",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 10,
                            "calories": 100
                        },
                        {
                            "name": "Squats",
                            "description": "A basic squat exercise",
                            "image_url": "https://img.freepik.com/premium-photo/fit-man-doing-squats_13339-265426.jpg",
                            "video_url": "https://www.youtube.com/watch?v=IB_icWRzi4E&pp=ygUGU3F1YXRz",
                            "reps": 20,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 150
                        },
                        {
                            "name": "Jumping Jacks",
                            "description": "A basic jumping jacks exercise",
                            "image_url": "https://hips.hearstapps.com/hmg-prod/images/portrait-of-barechested-muscular-man-practicing-royalty-free-image-1663776097.jpg?crop=0.668xw:1.00xh;0,0&resize=1200:*",
                            "video_url": "https://www.youtube.com/watch?v=CWpmIW6l-YA&pp=ygUNSnVtcGluZyBKYWNrcw%3D%3D",
                            "reps": 30,
                            "sets": 3,
                            "duration_minutes": 5,
                            "calories": 100
                        },
                        {
                            "name": "Plank",
                            "description": "A basic plank exercise",
                            "image_url": "https://www.shape.com/thmb/T2GyvzFah3XYR8_L8W16ANWBTXs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/low-plank-hold-b8a63da1ef844f00b6f6a21141ba1d87.jpg",
                            "video_url": "https://www.youtube.com/watch?v=pvIjsG5Svck&pp=ygUFcGxhbms%3D",
                            "reps": 1,
                            "sets": 3,
                            "duration_minutes": 5,
                            "calories": 50
                        },
                        {
                            "name": "Running",
                            "description": "Running at a moderate pace",
                            "image_url": "https://hips.hearstapps.com/hmg-prod/images/running-track-1667904802.jpg?crop=0.668xw:1.00xh;0.0737xw,0&resize=1200:*",
                            "video_url": "https://www.youtube.com/watch?v=_kGESn8ArrU&pp=ygUOaG93IHRvIHJ1bm5pbmc%3D",
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
                            "image_url": "https://www.jennycancook.com/wp-content/uploads/2013/05/GreenEggsNoHam_600_2.jpg",
                            "calories": 400,
                            "protein": 20,
                            "carbs": 30,
                            "fat": 15
                        },
                        {
                            "name": "Grilled chicken salad",
                            "description": "Lunch",
                            "image_url": "https://www.eatingwell.com/thmb/-aGwTbt7B4RQKFyiwptHchM07yc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/grilled-chicken-salad-8055766-4000x2700-a146f316698d4d26a1f35ecdd699cc94.jpg",
                            "calories": 600,
                            "protein": 40,
                            "carbs": 50,
                            "fat": 20
                        },
                        {
                            "name": "Protein shake",
                            "description": "Snack",
                            "image_url": "https://assets.tmecosys.com/image/upload/t_web767x639/img/recipe/ras/Assets/65b07d07-f394-4759-98e6-f9ca32dc2e80/Derivates/67394c62-fa3b-4271-9c36-6e107752e584.jpg",
                            "calories": 200,
                            "protein": 30,
                            "carbs": 10,
                            "fat": 5
                        },
                        {
                            "name": "Baked salmon with quinoa",
                            "description": "Dinner",
                            "image_url": "https://www.jessicagavin.com/wp-content/uploads/2016/02/mediterranean-spiced-salmon-over-vegetable-quinoa-1200.jpg",
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
                            "image_url": "https://www.mensjournal.com/wp-content/uploads/2018/05/1380-burpee1.jpg",
                            "video_url": "https://www.youtube.com/watch?v=auBLPXO8Fww&pp=ygUHQnVycGVlcw%3D%3D",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 10,
                            "calories": 150
                        },
                        {
                            "name": "Lunges",
                            "description": "A basic lunge exercise",
                            "image_url": "https://www.verywellfit.com/thmb/3Fr0PXhbiYn2-p86VQ0X3GGKx_o=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Lunges_annotated-a1293f16ceab4b8d8716e44bbfa58315.jpg",
                            "video_url": "https://www.youtube.com/watch?v=MxfTNXSFiYI&pp=ygUGTHVuZ2Vz",
                            "reps": 20,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 150
                        },
                        {
                            "name": "Mountain Climbers",
                            "description": "A basic mountain climber exercise",
                            "image_url": "https://images.livemint.com/img/2023/09/28/1140x641/Fitness_mountain_climbers_1695909933565_1695909946377.jpg",
                            "video_url": "https://www.youtube.com/watch?v=nmwgirgXLYM&pp=ygURTW91bnRhaW4gQ2xpbWJlcnM%3D",
                            "reps": 30,
                            "sets": 3,
                            "duration_minutes": 5,
                            "calories": 100
                        },
                        {
                            "name": "Bicycle Crunches",
                            "description": "A basic bicycle crunch exercise",
                            "image_url": "https://www.verywellfit.com/thmb/GKO4FQVMDwARAII73qjmXhUqlSM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/BicycleCrunches_annotated-b90ca5400452440282721a7d33d75b39.jpg",
                            "video_url": "https://www.youtube.com/watch?v=cbKIDZ_XyjY&pp=ygUQQmljeWNsZSBDcnVuY2hlcw%3D%3D",
                            "reps": 20,
                            "sets": 3,
                            "duration_minutes": 10,
                            "calories": 100
                        },
                        {
                            "name": "Jump Rope",
                            "description": "Jumping rope for cardio",
                            "image_url": "https://i5.walmartimages.com/asr/e94b589b-a716-48d2-9b4e-f1b1cbb16e95.94fc0880aebc10a20f7ede1fea59ae74.jpeg?odnHeight=768&odnWidth=768&odnBg=FFFFFF",
                            "video_url": "https://www.youtube.com/watch?v=FJmRQ5iTXKE&pp=ygUQaG93IHRvIEp1bXAgUm9wZQ%3D%3D",
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
                            "image_url": "https://nenaswellnesscorner.com/wp-content/uploads/2023/07/Oatmeal-with-fruit-n1.jpg",
                            "calories": 400,
                            "protein": 15,
                            "carbs": 70,
                            "fat": 10
                        },
                        {
                            "name": "Turkey sandwich with salad",
                            "description": "Lunch",
                            "image_url": "https://www.thespruceeats.com/thmb/nswVQ3ethledYcPs1nv-_z9sD2g=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/perfect-turkey-salad-sandwiches-3061907-hero-05-72d6a0529c3b4e50a70881ec00ed8738.jpg",
                            "calories": 600,
                            "protein": 35,
                            "carbs": 50,
                            "fat": 20
                        },
                        {
                            "name": "Greek yogurt with berries",
                            "description": "Snack",
                            "image_url": "https://healthywithachanceofsprinkles.com/wp-content/uploads/2021/09/Breakfast-without-Eggs-Greek-Yogurt-Berries-High-Protein-Breakfast.jpg",
                            "calories": 200,
                            "protein": 15,
                            "carbs": 30,
                            "fat": 5
                        },
                        {
                            "name": "Stir-fried tofu with vegetables",
                            "description": "Dinner",
                            "image_url": "https://omnivorescookbook.com/wp-content/uploads/2022/02/211213_Stir-Fried-Bok-Choy-With-Tofu-Puffs_550.jpg",
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
                            "image_url": "https://hardtokillfitness.co/cdn/shop/articles/deadlifts.png?v=1661801478",
                            "video_url": "https://www.youtube.com/watch?v=AweC3UaM14o&pp=ygUIRGVhZGxpZnQ%3D",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 200
                        },
                        {
                            "name": "Bench Press",
                            "description": "A basic bench press exercise",
                            "image_url": "https://www.anytimefitness.com/wp-content/uploads/2024/01/AF-HERO_BenchPress-1024x683.jpg",
                            "video_url": "https://www.youtube.com/watch?v=4Y2ZdHCOXok&pp=ygUSQmVuY2ggUHJlc3MgdmlkZW8g",
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
                            "image_url": "https://www.verywellfit.com/thmb/L8ErPvWV1_VqdZiD_GlGhUw1IuA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/About-2A15-TricepDips-935-e3cd3eddc0c149fc91299b420aa6b236.jpg",
                            "video_url": "https://www.youtube.com/watch?v=Tw0axi-Jlqc&pp=ygULVHJpY2VwIERpcHM%3D",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 10,
                            "calories": 100
                        },
                        {
                            "name": "Running",
                            "description": "Running at a moderate pace",
                            "image_url": "https://hips.hearstapps.com/hmg-prod/images/running-track-1667904802.jpg?crop=0.668xw:1.00xh;0.0737xw,0&resize=1200:*",
                            "video_url": "https://www.youtube.com/watch?v=kVnyY17VS9Y&pp=ygUOUnVubmluZyBob3cgdG8%3D",
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
                            "image_url": "https://www.wellplated.com/wp-content/uploads/2022/12/Smoothie-Bowl-For-Dinner-Healthy.jpg",
                            "calories": 400,
                            "protein": 20,
                            "carbs": 50,
                            "fat": 10
                        },
                        {
                            "name": "Chicken and brown rice",
                            "description": "Lunch",
                            "image_url": "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2013/12/27/0/FNK_baked-orange-chicken-and-brown-rice_s4x3.jpg.rend.hgtvcom.616.462.suffix/1389219144853.jpeg",
                            "calories": 600,
                            "protein": 40,
                            "carbs": 60,
                            "fat": 15
                        },
                        {
                            "name": "Protein bar",
                            "description": "Snack",
                            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Three_protein_bars.jpg/1200px-Three_protein_bars.jpg",
                            "calories": 200,
                            "protein": 20,
                            "carbs": 20,
                            "fat": 5
                        },
                        {
                            "name": "Beef stir-fry with vegetables",
                            "description": "Dinner",
                            "image_url": "https://cdn.momsdish.com/wp-content/uploads/2021/07/Steak-Stir-Fry-Recipe-014.jpg",
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
                            "image_url": "https://cdn.mos.cms.futurecdn.net/9ghCpUY6JaLtStkZkeH73T.jpg",
                            "video_url": "https://www.youtube.com/watch?v=IODxDxX7oi4&t=10s&pp=ygUHUHVzaC11cA%3D%3D",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 10,
                            "calories": 100
                        },
                        {
                            "name": "Squats",
                            "description": "A basic squat exercise",
                            "image_url": "https://blog.fitbit.com/wp-content/uploads/2016/10/ArmStanding.jpg",
                            "video_url": "https://www.youtube.com/watch?v=HFnSsLIB7a4&pp=ygUGU3F1YXRz",
                            "reps": 20,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 150
                        },
                        {
                            "name": "Jumping Jacks",
                            "description": "A basic jumping jacks exercise",
                            "image_url": "https://i0.wp.com/www.muscleandfitness.com/wp-content/uploads/2014/02/533_B.jpg?w=800&h=630&crop=1&quality=86&strip=all",
                            "video_url": "https://www.youtube.com/watch?v=CWpmIW6l-YA&pp=ygUNSnVtcGluZyBKYWNrcw%3D%3D",
                            "reps": 30,
                            "sets": 3,
                            "duration_minutes": 5,
                            "calories": 100
                        },
                        {
                            "name": "Plank",
                            "description": "A basic plank exercise",
                            "image_url": "https://blog-images-1.pharmeasy.in/blog/production/wp-content/uploads/2021/01/06152556/3.jpg",
                            "video_url": "https://www.youtube.com/watch?v=yeKv5oX_6GY&pp=ygUFUGxhbms%3D",
                            "reps": 1,
                            "sets": 3,
                            "duration_minutes": 5,
                            "calories": 50
                        },
                        {
                            "name": "Running",
                            "description": "Running at a moderate pace",
                            "image_url": "https://hips.hearstapps.com/hmg-prod/images/running-track-1667904802.jpg?crop=0.668xw:1.00xh;0.0737xw,0&resize=1200:*",
                            "video_url": "https://www.youtube.com/watch?v=kVnyY17VS9Y&pp=ygUOUnVubmluZyBob3cgdG8%3D",
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
                            "image_url": "https://www.slenderkitchen.com/sites/default/files/styles/gsd-1x1/public/recipe_images/veggie-scramble.jpeg",
                            "calories": 400,
                            "protein": 20,
                            "carbs": 30,
                            "fat": 15
                        },
                        {
                            "name": "Grilled chicken salad",
                            "description": "Lunch",
                            "image_url": "https://hips.hearstapps.com/hmg-prod/images/grilled-chicken-salad-index-6628169554c88.jpg?crop=0.8890484453220048xw:1xh;center,top&resize=1200:*",
                            "calories": 600,
                            "protein": 40,
                            "carbs": 50,
                            "fat": 20
                        },
                        {
                            "name": "Protein shake",
                            "description": "Snack",
                            "image_url": "https://www.eatingwell.com/thmb/JZ00DKa4QI8_hRstipASavKa9Pk=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/EWL-261428-chocolate-peanut-butter-protein-shake-Hero-02-e49db6f2f2db4c04b6f4807e54ca3ee0.jpg",
                            "calories": 200,
                            "protein": 30,
                            "carbs": 10,
                            "fat": 5
                        },
                        {
                            "name": "Baked salmon with quinoa",
                            "description": "Dinner",
                            "image_url": "https://www.seriouseats.com/thmb/pRFzs9JxSdwFgmcKcKh3Z1fsu3E=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__serious_eats__seriouseats.com__recipes__images__2013__03__20130308-skillet-suppers-salmon-quinoa1-92215fa78bc74c28b55b38e0dcefb0da.jpg",
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
                            "image_url": "https://marathonhandbook.com/wp-content/uploads/Benefits-Of-Burpees-2-1.jpg",
                            "video_url": "https://www.youtube.com/watch?v=auBLPXO8Fww&pp=ygUHQnVycGVlcw%3D%3D",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 10,
                            "calories": 150
                        },
                        {
                            "name": "Lunges",
                            "description": "A basic lunge exercise",
                            "image_url": "https://www.verywellfit.com/thmb/3Fr0PXhbiYn2-p86VQ0X3GGKx_o=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Lunges_annotated-a1293f16ceab4b8d8716e44bbfa58315.jpg",
                            "video_url": "https://www.youtube.com/watch?v=MxfTNXSFiYI&pp=ygUGTHVuZ2Vz",
                            "reps": 20,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 150
                        },
                        {
                            "name": "Mountain Climbers",
                            "description": "A basic mountain climber exercise",
                            "image_url": "https://hips.hearstapps.com/hmg-prod/images/rw-jess-mountain-climber-1596573079.jpg",
                            "video_url": "https://www.youtube.com/watch?v=De3Gl-nC7IQ&pp=ygURTW91bnRhaW4gQ2xpbWJlcnM%3D",
                            "reps": 30,
                            "sets": 3,
                            "duration_minutes": 5,
                            "calories": 100
                        },
                        {
                            "name": "Bicycle Crunches",
                            "description": "A basic bicycle crunch exercise",
                            "image_url": "https://www.verywellfit.com/thmb/GKO4FQVMDwARAII73qjmXhUqlSM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/BicycleCrunches_annotated-b90ca5400452440282721a7d33d75b39.jpg",
                            "video_url": "https://www.youtube.com/watch?v=1we3bh9uhqY&pp=ygUQQmljeWNsZSBDcnVuY2hlcw%3D%3D",
                            "reps": 20,
                            "sets": 3,
                            "duration_minutes": 10,
                            "calories": 100
                        },
                        {
                            "name": "Jump Rope",
                            "description": "Jumping rope for cardio",
                            "image_url": "https://go-zone.ca/cdn/shop/products/191730243376_1_2000x.jpg?v=1646754549",
                            "video_url": "https://www.youtube.com/watch?v=wqN5bRkZPK0&pp=ygUQanVtcCByb3BlIGhvdyB0bw%3D%3D",
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
                            "image_url": "https://nenaswellnesscorner.com/wp-content/uploads/2023/07/Oatmeal-with-fruit-n1.jpg",
                            "calories": 400,
                            "protein": 15,
                            "carbs": 70,
                            "fat": 10
                        },
                        {
                            "name": "Turkey sandwich with salad",
                            "description": "Lunch",
                            "image_url": "https://www.tasteofhome.com/wp-content/uploads/2018/01/exps44898_SD163324B08_06_1b-4.jpg",
                            "calories": 600,
                            "protein": 35,
                            "carbs": 50,
                            "fat": 20
                        },
                        {
                            "name": "Greek yogurt with berries",
                            "description": "Snack",
                            "image_url": "https://daisiesandpie.co.uk/wp-content/uploads/2015/04/Greek-yogurt-and-berries-768x1024-720x720.jpg",
                            "calories": 200,
                            "protein": 15,
                            "carbs": 30,
                            "fat": 5
                        },
                        {
                            "name": "Stir-fried tofu with vegetables",
                            "description": "Dinner",
                            "image_url": "https://hips.hearstapps.com/hmg-prod/images/190130-tofu-stir-fry-horizontal-150-1549302524.jpg?crop=1xw:0.843328335832084xh;center,top",
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
                            "image_url": "https://cali.vn/storage/app/media/deadlift-dung-cach-thumb.jpg",
                            "video_url": "https://www.youtube.com/watch?v=AweC3UaM14o&pp=ygUIRGVhZGxpZnQ%3D",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 200
                        },
                        {
                            "name": "Bench Press",
                            "description": "A basic bench press exercise",
                            "image_url": "https://www.anytimefitness.com/wp-content/uploads/2024/01/AF-HERO_BenchPress-1024x683.jpg",
                            "video_url": "https://www.youtube.com/watch?v=4Y2ZdHCOXok&pp=ygULQmVuY2ggUHJlc3M%3D",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 150
                        },
                        {
                            "name": "Bent Over Row",
                            "description": "A basic bent over row exercise",
                            "image_url": "https://cdn.shopify.com/s/files/1/1497/9682/files/2_30d219ed-3974-461b-9f14-d3d809da3c65.jpg?v=1647875300",
                            "video_url": "https://www.youtube.com/shorts/Nqh7q3zDCoQ",
                            "reps": 20,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 150
                        },
                        {
                            "name": "Tricep Dips",
                            "description": "A basic tricep dips exercise",
                            "image_url": "https://www.verywellfit.com/thmb/L8ErPvWV1_VqdZiD_GlGhUw1IuA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/About-2A15-TricepDips-935-e3cd3eddc0c149fc91299b420aa6b236.jpg",
                            "video_url": "https://www.youtube.com/watch?v=Tw0axi-Jlqc&t=1s&pp=ygULVHJpY2VwIERpcHM%3D",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 10,
                            "calories": 100
                        },
                        {
                            "name": "Running",
                            "description": "Running at a moderate pace",
                            "image_url": "https://hips.hearstapps.com/hmg-prod/images/running-track-1667904802.jpg?crop=0.668xw:1.00xh;0.0737xw,0&resize=1200:*",
                            "video_url": "https://www.youtube.com/watch?v=_kGESn8ArrU&pp=ygUOUnVubmluZyBob3cgdG8%3D",
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
                            "image_url": "https://images.immediate.co.uk/production/volatile/sites/30/2022/12/Smoothie-bowl-16df176.jpg",
                            "calories": 400,
                            "protein": 20,
                            "carbs": 50,
                            "fat": 10
                        },
                        {
                            "name": "Chicken and brown rice",
                            "description": "Lunch",
                            "image_url": "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2013/12/27/0/FNK_baked-orange-chicken-and-brown-rice_s4x3.jpg.rend.hgtvcom.616.462.suffix/1389219144853.jpeg",
                            "calories": 600,
                            "protein": 40,
                            "carbs": 60,
                            "fat": 15
                        },
                        {
                            "name": "Protein bar",
                            "description": "Snack",
                            "image_url": "ghttps://media.post.rvohealth.io/wp-content/uploads/2022/04/homemade-protein-bar-1200x628-facebook-1200x628.jpg",
                            "calories": 200,
                            "protein": 20,
                            "carbs": 20,
                            "fat": 5
                        },
                        {
                            "name": "Beef stir-fry with vegetables",
                            "description": "Dinner",
                            "image_url": "https://playswellwithbutter.com/wp-content/uploads/2022/02/Beef-and-Vegetable-Stir-Fry-16.jpg",
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
                            "image_url": "https://cdn.mos.cms.futurecdn.net/9ghCpUY6JaLtStkZkeH73T.jpg",
                            "video_url": "https://www.youtube.com/watch?v=-T64FLsJnAU&pp=ygUHUHVzaC11cA%3D%3D",
                            "reps": 15,
                            "sets": 3,
                            "duration_minutes": 10,
                            "calories": 100
                        },
                        {
                            "name": "Squats",
                            "description": "A basic squat exercise",
                            "image_url": "https://media.glamourmagazine.co.uk/photos/6138a5b2236c41e831489fec/16:9/w_2560%2Cc_limit/gettyimages-1219540136_sf.jpg",
                            "video_url": "https://www.youtube.com/watch?v=HFnSsLIB7a4&pp=ygUGU3F1YXRz",
                            "reps": 20,
                            "sets": 3,
                            "duration_minutes": 15,
                            "calories": 150
                        },
                        {
                            "name": "Jumping Jacks",
                            "description": "A basic jumping jacks exercise",
                            "image_url": "https://hips.hearstapps.com/hmg-prod/images/portrait-of-barechested-muscular-man-practicing-royalty-free-image-1663776097.jpg?crop=0.668xw:1.00xh;0,0&resize=1200:*",
                            "video_url": "https://www.youtube.com/watch?v=CWpmIW6l-YA&pp=ygUNSnVtcGluZyBKYWNrcw%3D%3D",
                            "reps": 30,
                            "sets": 3,
                            "duration_minutes": 5,
                            "calories": 100
                        },
                        {
                            "name": "Plank",
                            "description": "A basic plank exercise",
                            "image_url": "https://hips.hearstapps.com/hmg-prod/images/hdm119918mh15842-1545237096.png?crop=0.668xw:1.00xh;0.117xw,0&resize=1200:*",
                            "video_url": "https://www.youtube.com/watch?v=pvIjsG5Svck&pp=ygUFUGxhbms%3D",
                            "reps": 1,
                            "sets": 3,
                            "duration_minutes": 5,
                            "calories": 50
                        },
                        {
                            "name": "Running",
                            "description": "Running at a moderate pace",
                            "image_url": "https://hips.hearstapps.com/hmg-prod/images/running-track-1667904802.jpg?crop=0.668xw:1.00xh;0.0737xw,0&resize=1200:*",
                            "video_url": "https://www.youtube.com/watch?v=kVnyY17VS9Y&pp=ygUPUnVubmluZyBob3cgdG8g",
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
                            "image_url": "https://www.paleoplan.com/wp-content/uploads/2011/07/paleo-recipes_scrambled-eggs-vegetables-bacon.jpg",
                            "calories": 400,
                            "protein": 20,
                            "carbs": 30,
                            "fat": 15
                        },
                        {
                            "name": "Grilled chicken salad",
                            "description": "Lunch",
                            "image_url": "https://hips.hearstapps.com/hmg-prod/images/grilled-chicken-salad-index-6628169554c88.jpg?crop=0.8890484453220048xw:1xh;center,top&resize=1200:*",
                            "calories": 600,
                            "protein": 40,
                            "carbs": 50,
                            "fat": 20
                        },
                        {
                            "name": "Protein shake",
                            "description": "Snack",
                            "image_url": "https://www.eatingwell.com/thmb/JZ00DKa4QI8_hRstipASavKa9Pk=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/EWL-261428-chocolate-peanut-butter-protein-shake-Hero-02-e49db6f2f2db4c04b6f4807e54ca3ee0.jpg",
                            "calories": 200,
                            "protein": 30,
                            "carbs": 10,
                            "fat": 5
                        },
                        {
                            "name": "Baked salmon with quinoa",
                            "description": "Dinner",
                            "image_url": "https://www.coles.com.au/content/dam/coles/inspire-create/jan21-images/Jan21-baked-salmon-with-quinoa-salad-976x549.jpg",
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
