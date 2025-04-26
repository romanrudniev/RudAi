from django.shortcuts import render
from .forms import PromptForm
import openai
openai.api_key = ''
client = openai.OpenAI()

def home(request):
    response_text = None
    response_image = None

    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']

            completion = client.chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {"role": "developer", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )

            response_text = completion.choices[0].message

            # response_text = f"Ви написали: {prompt}"

    else:
        form = PromptForm()

    return render(request, 'home.html', {
        'form': form,
        'response_text': response_text,
        'response_image': response_image,
    })
