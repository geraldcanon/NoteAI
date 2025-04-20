from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import pytesseract
from PIL import Image
from NoteAI.function.fetchAI import fetchAI
# Create your views here.

def convert(file):
    text=""
    extracted = pytesseract.image_to_string(Image.open(file))
    text+=extracted
    return text

    
def imageconverter(request):
    if request.method =="POST":
        try:
            file = request.FILE.get("file")
            if not file:
                return JsonResponse({"error":"no file uploaded"},status=405)
            if file.name.endswith('png','jpeg','jpg','img'):
                data = convert(file)
            else:
                return JsonResponse({"error":"invalid file format"},status=405)
            
            
            prompt= (
                "Clearly explain the following topic in a formal, informative style. Do not use first-person phrases like 'I think' or 'I'm trying to understand'. Focus entirely on delivering a structured, professional explanation without conversational or reflective language: "
                + data
            )
            res = fetchAI(prompt)

            return JsonResponse({'discussion': res})

        except Exception as e:
            return JsonResponse({"error":e})
    return JsonResponse({"error":"Wrong request method"},status=405)