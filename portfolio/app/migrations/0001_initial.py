# Generated by Django 5.0.3 on 2024-03-12 05:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availablefor', models.CharField(max_length=200)),
                ('short_intro', models.TextField()),
                ('completedProjects', models.PositiveBigIntegerField()),
                ('clients', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='aboutme')),
                ('facebookUrl', models.URLField(blank=True, null=True)),
                ('instagramUrl', models.URLField(blank=True, null=True)),
                ('linkendinUrl', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('gmail', models.EmailField(max_length=254)),
                ('locationUrl', models.URLField(max_length=1050)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=300)),
                ('companyName', models.CharField(max_length=300)),
                ('startedDate', models.DateField()),
                ('endDate', models.DateField()),
                ('short_description_about_work', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=250)),
                ('short_Intro', models.TextField(max_length=600)),
                ('cv', models.FileField(upload_to='cv')),
                ('image', models.ImageField(upload_to='introimg/')),
                ('phoneNo', models.PositiveBigIntegerField()),
                ('address', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectType', models.CharField(choices=[('MobileApp', 'Mobile Application'), ('Website', 'Website')], max_length=150)),
                ('projectName', models.CharField(max_length=200)),
                ('languageUsed', models.TextField()),
                ('country', models.CharField(max_length=200)),
                ('projectUrl', models.URLField(blank=True, null=True)),
                ('short_description', models.TextField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('rateSkill_1to100', models.PositiveBigIntegerField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PortfolioImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Portfolioimage/')),
                ('portfolio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='portfolioimages', to='app.portfolio')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
