from django.shortcuts import render,redirect

# Create your views here.
def dash(request):
    return render(request,'dash.html')