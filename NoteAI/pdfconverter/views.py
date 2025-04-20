from django.shortcuts import render
from pdfconverter.functions.pdfToText import extract_from_docx as docsConverter
from pdfconverter.functions.pdfToText import extract_from_pdf as pdfConverter
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()


@csrf_exempt
def home(request):
    if request.method == "POST":
        try:
            file = request.FILES.get('file')
            if not file:
                return JsonResponse({"error": "No file uploaded"}, status=400)

            if file.name.endswith('.pdf'):
               data = pdfConverter(file)

            elif file.name.endswith('.docx'):
                data = docsConverter(file)
            else:
                return JsonResponse({"error": "Unsupported file type"}, status=400)

            prompt = "make a just straight up discussion and explaination ,theres no any word just the discussion: " + data

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
            return JsonResponse({'discussion': res})

        except Exception as e:
            return JsonResponse({"error":"mali din dito (2)"},{"error": str(e)}, status=500)

    return JsonResponse({"error": "mali dito (1)"}, status=405)