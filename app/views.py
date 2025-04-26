# Create your views here.

from django.shortcuts import render
from .forms import PromptFor

def home(request):
    response_text = None
    image_url = None

    if request.method == 'POST':
        form = PromptFor(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']

            # Поки що просто виводимо, що написав користувач
            response_text = f"Ви написали: {prompt}"

    else:
        form = PromptFor()

    return render(request, 'base.html', {
        'form': form,
        'response_text': response_text,
        'image_url': image_url,
    })
