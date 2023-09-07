from django.shortcuts import render

# Create your views here.

app_name = 'home'

def HomeView(request):
    return render(request, 'polyh/gabarit.html')