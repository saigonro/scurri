from django.shortcuts import render

# Create your views here.

def postcodesuk(request):
    return render(request, 'postcodesuk/postcodesuk.html')