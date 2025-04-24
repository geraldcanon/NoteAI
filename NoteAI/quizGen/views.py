from NoteAI.function.fetchAI import fetchAI

from django.http import JsonResponse

from dotenv import load_dotenv
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
load_dotenv()
# Create your views
@csrf_exempt
def generate_quiz(request):
    if request.method=="POST":

        try:
            data=json.loads(request.body)
   
            prompt =data.get('prompt','')
            if not prompt:
                return(JsonResponse({'error':'no prompt'},status=400))
            instruction = (
    "Generate a set of quiz questions (1-30), strictly based on the data provided. "
    "Ensure the output follows this exact format, with no additional information, commentary, or variation from the structure given below. "
    "Only the data you provide should be formatted exactly as shown:\n\n"
    "DATA_PASS\n"
    "===Discussion===\n"
    f"{prompt}\n\n"
    "[\n"
    "  {\n"
    '    "qa": "Your question here?",\n'
    '    "options": [\n'
    '      "a. Option 1",\n'
    '      "b. Option 2",\n'
    '      "c. Option 3",\n'
    '      "d. Option 4"\n'
    "    ],\n"
    '    "correctAnswer": 0\n'
    "  },\n"
    "]\n\n"
    'Each question must contain:\n'
    '"qa" - The question being asked.\n'
    '"options" - An array with exactly 4 options, each labeled \'a\', \'b\', \'c\', and \'d\'.\n'
    '"correctAnswer" - An integer value (0, 1, 2, or 3) representing the index of the correct answer from the "options" array.\n\n'
    "Question and answer should be found in one [] only, all questions are combined and doesnt have a seperate json "
    "Strictly follow this structure with no modifications. Provide only the output as shown, nothing more, nothing less."
)

         
            
            res = fetchAI(instruction)
            obj_json= json.loads(f"{res}")
            print(obj_json[0]["qa"])
           
            print(res)
            return JsonResponse({"data":obj_json })

        except Exception as e:
            print(e)
            return JsonResponse({'error':e}, status=405)

    return JsonResponse({'error': 'sira dito'}, status=405)
def home(request):
    return HttpResponse("<h1>Hello, World!</h1>")