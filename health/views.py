from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return redirect('accounts/home')

def unsubscribe(request):
    return render(request, 'health/unsubscribe.html')