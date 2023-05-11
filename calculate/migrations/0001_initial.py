# Generated by Django 4.2 on 2023-04-25 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h1', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('number', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('video', models.URLField(blank=True, max_length=100, null=True, verbose_name='url для видео')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h2', models.CharField(max_length=40)),
                ('content', models.TextField()),
                ('day', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='calculate.days')),
            ],
        ),
        migrations.CreateModel(
            name='Scrub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('instruction', models.TextField()),
                ('components', models.TextField()),
                ('train', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='calculate.train')),
            ],
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('callories', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('protein', models.DecimalField(decimal_places=1, max_digits=30)),
                ('fats', models.DecimalField(decimal_places=1, max_digits=30)),
                ('carbohydrates', models.DecimalField(decimal_places=1, max_digits=30)),
                ('video', models.URLField()),
                ('description', models.TextField()),
                ('train', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='nutrition', to='calculate.train')),
            ],
        ),
        migrations.CreateModel(
            name='Muscles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('exercise', models.ManyToManyField(related_name='muscles', to='calculate.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.CharField(choices=[('breakfast', 'breakfast'), ('lunch', 'lunch'), ('dinner', 'dinner'), ('snack', 'snack')], max_length=20)),
                ('day', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nutrition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='calculate.nutrition')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='train',
            field=models.ManyToManyField(related_name='exercises', to='calculate.train'),
        ),
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('calories', models.IntegerField()),
                ('meals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='calculate.meals')),
            ],
        ),
        migrations.CreateModel(
            name='DailyWater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.SmallIntegerField(default=0)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Advices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('exercise', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='advice', to='calculate.train')),
            ],
        ),
    ]