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
            prompt ="Just straight-up quiz, no introduction, just the quiz choices: "+data.get('prompt','')
            if not prompt:
                return(JsonResponse({'error':'no prompt'},status=400))
            
            res = fetchAI(prompt)

            return JsonResponse({'quiz': res})

        except Exception as e:
            return JsonResponse({'error':'mali ang structure ng prompt'}, status=405)

    return JsonResponse({'error': 'sira dito'}, status=405)
def home(request):
    return HttpResponse("<h1>Hello, World!</h1>")