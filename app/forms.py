from django import forms

class PromptFor(forms.Form):
    prompt = forms.CharField(label="Enter your prompt", max_length=750)