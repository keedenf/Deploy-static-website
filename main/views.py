from django.shortcuts import render

# Create your views here.
def home(request):
    '''Renders homepage'''
    return render(request, 'main/home.html', {})


def live(request):
    '''Renders live feed information'''
    return render(request, 'main/live.html', {})

