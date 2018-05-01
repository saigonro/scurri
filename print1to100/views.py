from django.shortcuts import render

# Create your views here.

def print1to100(request):
    numbers = list(range(1, 101))
    return render(request, 'print1to100/print1to100.html', {'numbers': numbers})
