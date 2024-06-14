from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from RevMeApp.models import Goal
from rest_framework.views import APIView   
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Handle POST requests without CSRF token
from .models import Goal, Assessment, Plan, Meal, Exercise, WorkoutPlan, MealPlan, Progress
from .serializers import AssessmentSerializer, GoalSerializer
from .utils import generate_plan
import pickle
import os
from dotenv import load_dotenv
import json

class AssessmentsList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        assessments = Assessment.objects.filter(user_id=request.user.id)
        serializer = AssessmentSerializer(assessments, many=True)
        return JsonResponse(serializer.data, safe=False)

class AssessmentsDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        assessment = Assessment.objects.get(pk=pk, user_id=request.user.id)
        serializer = AssessmentSerializer(assessment)
        return JsonResponse(serializer.data, safe=False)

class PredictObesity(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # Extract data from the request body (assuming JSON format)
        data = JSONParser().parse(request)
        # Create a Goal object from the received data
        assessment = Assessment(
            user_id=request.user.id,
            gender=data['Gender'],
            age=data['Age'],
            height=data['Height'],
            weight=data['Weight'],
            CALC=data['CALC'],
            FAVC=data['FAVC'],
            FCVC=data['FCVC'],
            NCP=data['NCP'],
            SCC=data['SCC'],
            SMOKE=data['SMOKE'],
            CH2O=data['CH2O'],
            family_history_with_overweight=data['family_history_with_overweight'],
            FAF=data['FAF'],
            TUE=data['TUE'],
            CAEC=data['CAEC'],
            MTRANS=data['MTRANS'],
        )
        # print(request.user.id)
        # print(assessment)

        assessment.save()
        load_dotenv()
        path_pkl = os.getenv("Path_model_ML")
        model = pickle.load(open(path_pkl, "rb"))

        if assessment.gender == "Male" :
            gender = 1
        elif assessment.gender == "Female": 
            gender = 0

        if assessment.CALC == "Always" :
            CALC = 0
        elif assessment.CALC == "Frequently": 
            CALC = 1
        elif assessment.CALC == "Sometimes":
            CALC = 2
        elif assessment.CALC == "no":
            CALC = 3 
        
        if assessment.FAVC == "no" :
            FAVC = 0
        elif assessment.FAVC == "yes": 
            FAVC = 1
            
        if assessment.SCC == "no" :
            SCC = 0
        elif assessment.SCC == "yes": 
            SCC = 1
            
        if assessment.SMOKE == "no" :
            SMOKE = 0
        elif assessment.SMOKE == "yes": 
            SMOKE = 1
            
        if assessment.family_history_with_overweight == "no" :
            family_history_with_overweight = 0
        elif assessment.family_history_with_overweight == "yes": 
            family_history_with_overweight = 1
            
        if assessment.CAEC == "Always" :
            CAEC = 0
        elif assessment.CAEC == "Frequently": 
            CAEC = 1
        elif assessment.CAEC == "Sometimes":
            CAEC = 2
        elif assessment.CAEC == "no":
            CAEC = 3    
        
        if assessment.MTRANS == "Automobile" :
            MTRANS = 0
        elif assessment.MTRANS == "Bike": 
            MTRANS = 1
        elif assessment.MTRANS == "Motorbike":
            MTRANS = 2
        elif assessment.MTRANS == "Public_Transportation":
            MTRANS = 3
        elif assessment.MTRANS == "Walking":
            MTRANS = 4

        # Extract features from the Assessment object
        features = [gender, assessment.age, assessment.height, assessment.weight, CALC, FAVC, assessment.FCVC, assessment.NCP, SCC, SMOKE, assessment.CH2O, family_history_with_overweight, assessment.FAF, assessment.TUE, CAEC, MTRANS]
        # print(features)
        # Use the model to predict obesity_lv
        predicted_obesity_lv = model.predict([features])[0]

        # Save the prediction to the database (if needed)
        assessment.NObeyesdad = predicted_obesity_lv

        if predicted_obesity_lv == 0:
            assessment.NObeyesdad = "Insufficient Weight"
            goal_type = "tăng cân"
            target_weight = 5
            duration_weeks = 12
            advice = ("You are underweight. Ensure you are eating enough nutritious food and consult a doctor or nutritionist for a proper diet plan. "
                    "Your goal is to gain weight. "
                    f"Target weight: {assessment.weight + target_weight} kg, duration: {duration_weeks} weeks.")
        elif predicted_obesity_lv == 1:
            assessment.NObeyesdad = "Normal Weight"
            goal_type = "duy trì"
            target_weight = 0
            duration_weeks = 0
            advice = ("You have a normal weight. Maintain a healthy lifestyle by continuing to eat a balanced diet and exercise regularly. "
                    "Your goal is to maintain your current weight. "
                    f"Target weight: {assessment.weight} kg.")
        elif predicted_obesity_lv == 2:
            assessment.NObeyesdad = "Obesity Level I"
            goal_type = "giảm cân"
            target_weight = 5
            duration_weeks = 12 
            advice = ("You are at Obesity Level I. Consider lifestyle changes such as increasing physical activity and reducing calorie intake. "
                    "Consult a doctor or nutritionist for a safe weight loss plan. "
                    f"Your goal is to lose weight. Target weight: {assessment.weight - target_weight} kg, duration: {duration_weeks} weeks.")
        elif predicted_obesity_lv == 3:
            assessment.NObeyesdad = "Obesity Level II"
            goal_type = "giảm cân"
            target_weight = 10
            duration_weeks = 24  
            advice = ("You are at Obesity Level II. Weight loss is important for your health. Seek support from healthcare professionals to develop an effective and safe weight loss plan. "
                    f"Your goal is to lose weight. Target weight: {assessment.weight - target_weight} kg, duration: {duration_weeks} weeks.")
        elif predicted_obesity_lv == 4:
            assessment.NObeyesdad = "Obesity Level III"
            goal_type = "giảm cân"
            target_weight = 15
            duration_weeks = 32 
            advice = ("You are at Obesity Level III. Significant weight loss is important for your health. Seek support from healthcare professionals to develop an effective and safe weight loss plan. "
                    "Focus on long-term lifestyle changes, including a healthy diet and regular physical activity. "
                    f"Your goal is to lose weight. Target weight: {assessment.weight - target_weight} kg, duration: {duration_weeks} weeks.")
        elif predicted_obesity_lv == 5:
            assessment.NObeyesdad = "Overweight Type I"
            goal_type = "giảm cân"
            target_weight = 3  
            duration_weeks = 8  
            advice = ("You are at Overweight Type I. Start by improving your diet and increasing physical activity. Small lifestyle changes can lead to positive results. "
                    f"Your goal is to lose weight. Target weight: {assessment.weight - target_weight} kg, duration: {duration_weeks} weeks.")
        elif predicted_obesity_lv == 6:
            assessment.NObeyesdad = "Overweight Type II"
            goal_type = "giảm cân"
            target_weight = 7
            duration_weeks = 16  
            advice = ("You are at Overweight Type II. Consider changing your diet and engaging in regular physical activity. Consulting a nutritionist can help you achieve your health goals. "
                    f"Your goal is to lose weight. Target weight: {assessment.weight - target_weight} kg, duration: {duration_weeks} weeks.")

        # Update assessment.NObeyesdad in the database
        assessment.save()

        # Return the prediction to the Android app
        return JsonResponse({'obesity_lv': assessment.NObeyesdad, "advice": advice , "goal_type": goal_type, "target_weight": target_weight, "duration_weeks": duration_weeks}, status=200)

class GeneratePlanAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = GoalSerializer(data=data)
        if serializer.is_valid():
            if not Goal.objects.filter(user_id=request.user.id, goal_type=data['goal_type']).exists():
                serializer.save(user_id=request.user.id)
            print("saved")
            user_data = Assessment.objects.filter(user_id=request.user.id).first()
            goal_data = Goal.objects.filter(user_id=request.user.id, goal_type=data['goal_type']).first()
            print("get ass and goal success")
            plan = generate_plan(goal_data, user_data)
            print("generate success")
            print(plan)
            print(json.dumps(plan, indent=4))
            # self.save_plan_to_db(request.user, goal_data, plan)
            return JsonResponse(plan, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    def save_plan_to_db(self, user, goal, plan):
        for day_plan in plan["plan"]:
            plan = Plan.objects.create(
                user = user,
                goal = goal, 
                name_day = day_plan["name_day"],
                description=day_plan["description"],
                calories_burned_per_day=day_plan["calories_burned_per_day"],
                calories_intake_per_day=day_plan["calories_intake_per_day"],
                created_at=timezone.now()
            )
            
            for workout in day_plan["workout"]:
                exercise, created = Exercise.objects.get_or_create(
                    name = workout["name"],
                    defaults = {
                        "description": workout.get("description", ""),
                        "image_url": workout.get("image_url", ""),
                        "video_url": workout.get("video_url", ""),
                        "reps": workout["reps"],
                        "sets": workout["sets"],
                        "duration_minutes": workout["duration_minutes"],
                        "calories": workout["calories"],
                        "created_at": timezone.now()
                    }
                )
                WorkoutPlan.objects.create(
                    plan = plan,
                    exercise = exercise,
                    note = "Generated by RevMe AI",
                    status = False,
                    update_at = timezone.now()
                )
                
            for meal in day_plan["meal"]:
                meal_obj, created = Meal.objects.get_or_create(
                    name = meal["name"],
                    defaults = {
                        "description": meal.get("description", ""),
                        "image_url": meal.get("image_url", ""),
                        "calories": meal["calories"],
                        "protein": meal["protein"],
                        "carbs": meal["carbs"],
                        "fat": meal["fat"],
                        "created_at": timezone.now()
                    }
                )
                MealPlan.objects.create(
                    plan = plan,
                    meal = meal_obj,
                    status = False,
                    note = "Generated by RevMe AI",
                    created_at = timezone.now()
                )
            
            Progress.objects.create(
                plan = plan,
                completed_workouts=0,
                completed_meals=0,
                total_calories_burned=0.0,
                total_calories_intake=0.0,
                total_water_intake=0.0,
                notes="Initial progress",
                update_at=timezone.now()
            )

