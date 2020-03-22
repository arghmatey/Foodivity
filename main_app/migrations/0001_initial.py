# Generated by Django 3.0.4 on 2020-03-22 20:44

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
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('type_activity', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('calories_burned', models.IntegerField()),
                ('activity_intensity', models.CharField(choices=[('L', 'light'), ('M', 'moderate'), ('S', 'strenuous'), ('V', 'very strenuous')], default=0, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('activity_level', models.CharField(choices=[('L', 'low'), ('M', 'moderate'), ('H', 'high')], default=0, max_length=1)),
                ('sex', models.CharField(choices=[('M', 'male'), ('F', 'female')], default=0, max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=25)),
                ('ingredients', models.CharField(max_length=100)),
                ('calories', models.IntegerField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profile')),
            ],
        ),
    ]
