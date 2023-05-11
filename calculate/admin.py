from django.contrib import admin
from .models import *

@admin.register(Days)
class TrainingsAdmin(admin.ModelAdmin):
    pass

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    pass

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass

@admin.register(Advices)
class AdvicesAdmin(admin.ModelAdmin):
    pass

@admin.register(Muscles)
class MusculesAdmin(admin.ModelAdmin):
    pass

@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    pass

@admin.register(Meals)
class MealsAdmin(admin.ModelAdmin):
    pass

@admin.register(Nutrition)
class NutritionAdmin(admin.ModelAdmin):
    pass

@admin.register(Ingredients)
class IngridientsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Scrub)
admin.site.register(DailyWater)
