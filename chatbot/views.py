from django.shortcuts import render
from django.http import JsonResponse
import openai

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]   
    )
    return response.choices[0].message.content.strip()

def chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        chatbot_response = chat_with_gpt(user_input)
        return JsonResponse({'chatbot_response': chatbot_response})
    return render(request, 'chatbot/index.html')