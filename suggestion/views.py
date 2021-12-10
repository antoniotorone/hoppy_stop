from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import ProductSuggestion
from .forms import SuggestionForm

""" Function that submit the suggestion\
    form and return to the template """


def add_suggestion(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == "POST":
            form = SuggestionForm(request.POST or None)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = user
                form.save()
                messages.success(request, 'Thank you for your suggestion')
            else:
                messages.error(request, 'Failed to send your suggestion.\
                Please check your form and try again')
        else:
            form = SuggestionForm()
        template = 'suggestion/suggestion.html'
        context = {
            'form': form,
        }

        return render(request, template, context)
