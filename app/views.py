from django.shortcuts import render, redirect
from .forms import PromptForm, RegisterForm, LoginForm
from django.contrib.auth import authenticate, login
import openai
# openai.api_key = ''
# client = openai.OpenAI()

def home(request):
    response_text = None
    response_image = None

    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']

            # completion = client.chat.completions.create(
            #     model="gpt-4.1",
            #     messages=[
            #         {"role": "developer", "content": "You are a helpful assistant."},
            #         {"role": "user", "content": prompt}
            #     ]
            # )
            #
            # response_text = completion.choices[0].message

            response_text = f"Ви написали: {prompt}"

    else:
        form = PromptForm()

    return render(request, 'home.html', {
        'form': form,
        'response_text': response_text,
        'response_image': response_image,
    })


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})