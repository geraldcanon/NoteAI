from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from groq import Groq
from dotenv import load_dotenv
import json
import os
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
load_dotenv()
# Create your views
@csrf_exempt
def generate_quiz(request):
    if request.method=="POST":

        try:
            data=json.loads(request.body)
            prompt ="Just straight-up quiz, no introduction, just the quiz choices: "+data.get('prompt','')
            if not prompt:
                return(JsonResponse({'error':'no prompt'},status=400))
            

            client = Groq(api_key=os.getenv("api_key"))

            
            completion = client.chat.completions.create(
                model="deepseek-r1-distill-llama-70b",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.6,
                max_tokens=1024,
                top_p=1,
                stream=False,
                stop=None,
            )
            res = completion.choices[0].message.content
            return JsonResponse({'quiz': res})

        except Exception as e:
            return JsonResponse({'error':'mali ang structure ng prompt'}, status=405)

    return JsonResponse({'error': 'sira dito'}, status=405)
def home(request):
    return HttpResponse("<h1>Hello, World!</h1>")