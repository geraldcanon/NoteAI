from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from groq import Groq
from dotenv import load_dotenv
import json
load_dotenv()
# Create your views
def generate_quiz(request):
    if request.methods=="POST":

        try:
            data=json.loads(request.body)
            prompt =data.get('prompt','')
            if not prompt:
                return(JsonResponse({'error':'no prompt'},status=400))
            

            client = Groq(api_key=os.getenv("api_key"))

            
            completion = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[{"role": "user", "content": prompt}],
                temperature=1,
                max_tokens=1024,
                top_p=1,
                stream=False,
                stop=None,
            )
            res = completion.choices[0].message.content
            return JsonResponse({'quiz': res})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
