from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from RevMeApp.models import Goal
from rest_framework.views import APIView   
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Handle POST requests without CSRF token
from .models import Goal, Assessment
from .utils import generate_plan
import pickle




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

        assessment.save()
        
        model = pickle.load(open("/Users/thanhduonghoang/Desktop/RevMe/RevMeApp/RFC.pkl", "rb"))

        if assessment.gender == "Male" :
            assessment.gender = 1
        elif assessment.gender == "Female": 
            assessment.gender = 0
            
        if assessment.CALC == "Always" :
            assessment.CALC = 0
        elif assessment.CALC == "Frequently": 
            assessment.CALC = 1
        elif assessment.CALC == "Sometimes":
            assessment.CALC = 2
        elif assessment.CALC == "no":
            assessment.CALC = 3 
        
        if assessment.FAVC == "no" :
            assessment.FAVC = 0
        elif assessment.FAVC == "yes": 
            assessment.FAVC = 1
            
        if assessment.SCC == "no" :
            assessment.SCC = 0
        elif assessment.SCC == "yes": 
            assessment.SCC = 1
            
        if assessment.SMOKE == "no" :
            assessment.SMOKE = 0
        elif assessment.SMOKE == "yes": 
            assessment.SMOKE = 1
            
        if assessment.family_history_with_overweight == "no" :
            assessment.family_history_with_overweight = 0
        elif assessment.family_history_with_overweight == "yes": 
            assessment.family_history_with_overweight = 1
            
        if assessment.CAEC == "Always" :
            assessment.CAEC = 0
        elif assessment.CAEC == "Frequently": 
            assessment.CAEC = 1
        elif assessment.CAEC == "Sometimes":
            assessment.CAEC = 2
        elif assessment.CAEC == "no":
            assessment.CAEC = 3    
        
        if assessment.MTRANS == "Automobile" :
            assessment.MTRANS = 0
        elif assessment.MTRANS == "Bike": 
            assessment.MTRANS = 1
        elif assessment.MTRANS == "Motorbike":
            assessment.MTRANS = 2
        elif assessment.MTRANS == "Public_Transportation":
            assessment.MTRANS = 3
        elif assessment.MTRANS == "Walking":
            assessment.MTRANS = 4

        
        # Extract features from the Assessment object
        features = [assessment.gender,assessment.age, assessment.height, assessment.weight, assessment.CALC, assessment.FAVC, assessment.FCVC, assessment.NCP, assessment.SCC, assessment.SMOKE, assessment.CH2O, assessment.family_history_with_overweight, assessment.FAF, assessment.TUE, assessment.CAEC, assessment.MTRANS]
        print(features)
        # Use the model to predict obesity_lv
        predicted_obesity_lv = model.predict([features])[0]

        # Save the prediction to the database (if needed)
        assessment.NObeyesdad = predicted_obesity_lv
        
        if predicted_obesity_lv == 0:
            assessment.NObeyesdad = "Insufficient Weight"
            advice = "You are underweight. Ensure you are eating enough nutritious food and consult a doctor or nutritionist for a proper diet plan."
        elif predicted_obesity_lv == 1:
            assessment.NObeyesdad = "Normal Weight"
            advice = "You have a normal weight. Maintain a healthy lifestyle by continuing to eat a balanced diet and exercise regularly."
        elif predicted_obesity_lv == 2:
            assessment.NObeyesdad = "Obesity Level I"
            advice = "You are at Obesity Level I. Consider lifestyle changes such as increasing physical activity and reducing calorie intake. Consult a doctor or nutritionist for a safe weight loss plan."
        elif predicted_obesity_lv == 3:
            assessment.NObeyesdad = "Obesity Level II"
            advice = "You are at Obesity Level II. Weight loss is important for your health. Seek support from healthcare professionals to develop an effective and safe weight loss plan."
        elif predicted_obesity_lv == 4:
            assessment.NObeyesdad = "Overweight Type I"
            advice = "You are at Overweight Type I. Start by improving your diet and increasing physical activity. Small lifestyle changes can lead to positive results."
        elif predicted_obesity_lv == 5:
            assessment.NObeyesdad = "Overweight Type II"
            advice = "You are at Overweight Type II. Consider changing your diet and engaging in regular physical activity. Consulting a nutritionist can help you achieve your health goals."
        elif predicted_obesity_lv == 6:
            assessment.NObeyesdad = "Overweight Type III"
            advice = "You are at Overweight Type III. Lifestyle changes are necessary to improve your health. Focus on eating healthy and being physically active. Support from healthcare professionals can help you develop a safe and effective weight loss plan."

        
        # Update assessment.NObeyesdad in the database
        assessment.save()

        # Return the prediction to the Android app
        return JsonResponse({'obesity_lv': assessment.NObeyesdad, "advice": advice }, status=200)


@csrf_exempt
@api_view(['GET'])
def plan_WD(request, user_id):
    try:
        goal_data = Goal.objects.filter(user_id=user_id).values()
    except Goal.DoesNotExist:
        return JsonResponse({'error': 'Goal not found'}, status=404)
    
    goal_data = list(goal_data) # convert QuerySet -> list of dictionaries
    plan = generate_plan(goal_data) # Call func generate_plan get plan workout and diet

    # Return data JSON format 
    return JsonResponse(plan, safe=False)
