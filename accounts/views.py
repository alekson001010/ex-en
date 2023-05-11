from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

def success(request, data):
    context = data
    return render(request, 'accounts/success.html', context)

import random
@csrf_exempt
def registerUser(request):
    User = get_user_model()
    if request.POST:
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            context = {'message': 'already exist'}
            return render(request, 'accounts/home.html', context=context)
        password = ''
        for x in range(10):  # Количество символов (16)
            password = password + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
        user = User.objects.create_user(email, password)
        login(request, user)
        user.set_password(password)
        context = {'email': email, 'password': password}
        return render(request, 'accounts/success.html', context=context)
    else:
        context = {}
    return render(request, 'accounts/home.html')


@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/calculate/days')
        else:
            return redirect('/accounts/login')
    else:
        return render(request, 'accounts/login.html')

import json
@csrf_exempt
def set_data(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    height = body.get('height')
    if height:
        request.user.height = height
        request.user.save()
    weight = body.get('weight')
    if weight:
        request.user.current_weight = weight
        request.user.save()
    age = body.get('age')
    if age:
        request.user.age = age
        request.user.save()
    target = body.get('target')
    dailyCalories = body.get('dailyCalories')
    if dailyCalories:
        request.user.dailyCalories = dailyCalories
        request.user.save()
    if target:
        if target == 0.5:
            request.user.goal = 'decrease'
            request.user.save()
        elif target == 1:
            request.user.goal = 'maintain'
            request.user.save()
        elif target == 1.5:
            request.user.goal = 'increase'
            request.user.save()
    return HttpResponse(status=204)

@csrf_exempt
def set_weight(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    field, value = body.get('field'), body.get('value')
    if field == 'start':
        request.user.initial_weight = value
        request.user.save()
    elif field == 'new':
        request.user.current_weight = value
        request.user.save()
    elif field == 'idea':
        request.user.target_weight = value
        request.user.save()
    return HttpResponse(status=204)


def logoutUser(request):
    logout(request)
    return redirect('/accounts/home')

@csrf_exempt
def passwordChange(request):
    if request.POST:
        old_password = request.POST["current-password"]
        new_password = request.POST["new-password"]
        new_password2 = request.POST["new-password-onemore"]
        if old_password != request.user.password:
            context = {
                "message": "Не правильный старый пароль"
            }
            return render(request, 'accounts/password.html', context=context)
        else:
            if new_password == new_password2:
                request.user.set_password(new_password2)
                request.user.save()
                return redirect('/')
            else:
                context = {
                    "message": "Новые пароли не совпадают"
                }
                return render(request, 'accounts/password.html', context=context)
    else:
        return render(request, 'accounts/password.html', context={})