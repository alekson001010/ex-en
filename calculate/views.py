from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Days, Train, Meals, Dishes, DailyWater
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def index(request):
    return render(request, 'calculate/index.html')

class DaysList(ListView):
    model = Days


    def get_context_data(self, **kwargs):
        context = super(DaysList, self).get_context_data(**kwargs) # get the default context data
        user = get_user_model().objects.get(id=self.request.user.id)
        if user.is_subscribed:
            days = user.date_subscribe
            days = datetime.now().date() - days
            days = days.days + 7
        else:
            days = 0
        context['allow_days'] = days
        return context

class DaysDetail(DetailView):
    model = Train

