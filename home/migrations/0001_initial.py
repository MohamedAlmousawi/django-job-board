# Generated by Django 4.0.5 on 2022-06-23 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('job_type', models.CharField(blank=True, choices=[('Full-Time', 'Full-time'), ('Part-Time', 'Part-Time')], max_length=50, null=True)),
                ('pulished_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('vacancy', models.IntegerField(blank=True, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='job_images')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=50)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='job_cv')),
                ('cover_letter', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.job')),
            ],
        ),
    ]