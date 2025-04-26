from django.shortcuts import render
from .forms import PromptForm
from openai import OpenAI

def home(request):
    response_text = None
    response_image = None

    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']

            response_text = f"Ви написали: {prompt}" #Виводить те що ми написали

    else:
        form = PromptForm()

    return render(request, 'home.html', {
        'form': form,
        'response_text': response_text,
        'response_image': response_image,
    })
