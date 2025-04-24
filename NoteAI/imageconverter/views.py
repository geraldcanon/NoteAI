from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import pytesseract
from PIL import Image
from NoteAI.function.fetchAI import fetchAI
# Create your views here.

def convert(file):
    text=""
    extracted = pytesseract.image_to_string(Image.open(file),lang='eng')
    text+=extracted
    return text

# @csrf_exempt   
# def imageconverter(request):
#     if request.method =="POST":
#         try:
#             file = request.FILES.get("file")
#             if not file:
#                 return JsonResponse({"error":"no file uploaded"},status=405)
#             if file.name.lower().endswith(('png','jpeg','jpg')):
#                 data = convert(file)
#             else:
#                 return JsonResponse({"error":"invalid file format"},status=405)
            
  

#             prompt= ( "Clearly explain the following topic in a formal, informative style. Do not use first-person phrases like 'I think' or 'I'm trying to understand'. Focus entirely on delivering a structured, professional explanation without conversational or reflective language Also Below Add a detailed notes in bullet form or not its up to you: "+
            
#                  data
#             )
            
#             res = fetchAI(prompt)
#             print(res)

#             return JsonResponse({'discussion': res})

#         except Exception as e:
#             print(e)
#             return JsonResponse({"error":e})
#     return JsonResponse({"error":"Wrong request method"},status=405)