
from pdfconverter.functions.pdfToText import extract_from_docx as docsConverter
from pdfconverter.functions.pdfToText import extract_from_pdf as pdfConverter
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from NoteAI.function.fetchAI import fetchAI
from imageconverter.views import convert

@csrf_exempt
def home(request):
    if request.method == "POST":
        try:
            file = request.FILES.get('file')
            if not file:
                return JsonResponse({"error": "No file uploaded"}, status=400)
            if file.name.endswith('.pdf'):
               data = pdfConverter(file)
            elif file.name.lower().endswith(('png','jpeg','jpg')):

                data=convert(file)

            elif file.name.endswith('.docx'):
                data = docsConverter(file)
            else:
                return JsonResponse({"error": "Unsupported file type"}, status=400)

            prompt = (
            "Clearly explain the following topic in a formal, informative style. Do not use first-person phrases like 'I think' or 'I'm trying to understand'. Focus entirely on delivering a structured, professional explanation without conversational or reflective language Also Below Add a extremely detailed notes  then expand it in a way that any can grasp in bullet form the label should be 'explanation' in the bullet explanation: "
            + data
        )
            res = fetchAI(prompt)
            print(file.name)
            print(res)


     
            return JsonResponse({'discussion': res})

        except Exception as e:
            return JsonResponse({"error":"mali din dito (2)"},{"error": str(e)}, status=500)

    return JsonResponse({"error": "mali dito (1)"}, status=405)