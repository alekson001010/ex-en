from django.db import models
from django.contrib.auth import get_user_model

user_model = get_user_model()


class Days(models.Model):
    h1 = models.CharField(max_length=40)
    description = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    number = models.IntegerField(default=1)

    def __str__(self):
        return self.h1

class Train(models.Model):
    day = models.OneToOneField(Days, on_delete=models.CASCADE)
    h2 = models.CharField(max_length=40)
    content = models.TextField()

    def __str__(self):
        return self.h2

class Exercise(models.Model):
    train = models.ManyToManyField(Train, related_name='exercises')
    name = models.CharField(max_length=50)
    video = models.URLField(max_length=100, verbose_name='url для видео', null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.name


'здесь советы к упражнению, их может быть несколько и их всегда разное кол-во решил вынести в отдельную таблицу'
class Advices(models.Model):
    exercise = models.OneToOneField(Train, on_delete=models.CASCADE, related_name='advice')
    content = models.TextField()

class Muscles(models.Model):
    name = models.CharField(max_length=40)
    exercise = models.ManyToManyField(Exercise, related_name='muscles')


class Meals(models.Model):
    choices = [
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner'),
        ('snack', 'snack'),
    ]
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    meal = models.CharField(max_length=20, choices=choices)
    day = models.DateField()

    def __str__(self):
        return f'{self.day} : {self.meal}'

class DailyWater(models.Model):
    volume = models.SmallIntegerField(default=0)
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    date = models.DateField()

class Dishes(models.Model):
    meals = models.ForeignKey(Meals, on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField(max_length=50)
    calories = models.IntegerField()

    def __str__(self):
        return f'{self.meals.meal} : {self.name}'

# class Scrub(models.Model):
#     name = models.CharField(max_length=100)
#     compound = models.CharField(max_length=255)
#     image = models.ImageField(null=True, blank=True)
#     technik = models.TextField()

class Nutrition(models.Model):
    train = models.OneToOneField(Train, on_delete=models.CASCADE, related_name='nutrition')
    name = models.CharField(max_length=50)
    callories = models.IntegerField()
    image = models.ImageField()
    protein = models.DecimalField(decimal_places=1, max_digits=30)
    fats = models.DecimalField(decimal_places=1, max_digits=30)
    carbohydrates = models.DecimalField(decimal_places=1, max_digits=30)
    video = models.URLField()
    description = models.TextField()

class Ingredients(models.Model):
    nutrition = models.ForeignKey(Nutrition, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=100)

class Scrub(models.Model):
    train = models.OneToOneField(Train, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField()
    instruction = models.TextField()
    components = models.TextField()

# нужно сделать так чтообы блюда относились к одному пользователю как и вода