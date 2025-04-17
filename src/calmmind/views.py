from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
import os


# Create your views here.
def home(request):
    return render(request, 'home.html')


def calmmindbot_response(request):
    if request.method == 'POST':
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        user_input = request.POST.get('user_input')
        # Get the selected model from the request
        model = request.POST.get('model', 'gpt-3.5-turbo')
        print(f"Selected model: {model}")
        
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model=model,  # Use the selected model
        )

        calmmind_reply = response.choices[0].message.content

        return JsonResponse({'reply': calmmind_reply})

    return render(request, 'calmmind/chat.html')
