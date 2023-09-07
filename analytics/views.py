from django.shortcuts import render

# Create your views here.


#Load Home Center
def Homeanalytics(request):
    return render(request, 'analytics/gabarit.html')
