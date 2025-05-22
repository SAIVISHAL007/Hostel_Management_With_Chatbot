import json
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .chatbot import get_chatbot_response

@method_decorator(csrf_exempt, name='dispatch')
class ChatbotView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            message = data.get('message', '')
            response = get_chatbot_response(message)
            return JsonResponse({'response': response})
        except Exception as e:
            return JsonResponse({'response': f'Error: {str(e)}'}, status=500)



def chatbot_page(request):
    return render(request, "chatbot.html")

