from django.shortcuts import render, redirect
from project.settings import API_KEY
from .forms import PromptForm, RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
import openai
from django.contrib import messages
import base64

# openai.api_key = ''
client = openai.OpenAI(api_key=API_KEY)

def home(request):
    response_text = None
    response_image = None
    error_message = None

    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            selected_model = form.cleaned_data['model_type']


            # gpt-3.5-turbo", "gpt-4.1
            try:
                if selected_model in ["gpt-3.5-turbo", "gpt-4.1"]:
                    completion = client.chat.completions.create(
                        model=selected_model,
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    response_text = completion.choices[0].message.content


                # dall-e-3
                elif selected_model == "dall-e-3":
                    image_result = client.images.generate(
                        model="dall-e-3",
                        prompt=prompt
                    )
                    response_image = image_result.data[0].url


                # gpt-image-1
                completion = client.chat.completions.create(
                    model="gpt-image-1",
                    messages=[
                        {"role": "system", "content": "You are an AI that generates images based on user input."},
                        {"role": "user", "content": prompt}
                    ]
                )
                image_url = completion.choices[0].message.content.strip()
                response_image = image_url

            except Exception as e:
                error_message = str(e)
    else:
        selected_model = request.GET.get('model_type', 'gpt-3.5-turbo')
        form = PromptForm(initial={'model_type': selected_model})

    return render(request, 'home.html', {
        'form': form,
        'response_text': response_text,
        'response_image': response_image,
        'error_message': error_message,
    })

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registration successful! Now log in.")
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
                messages.success(request, f"Welcome, {username}!")
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')