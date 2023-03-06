# Generated by Django 2.2.13 on 2023-02-21 11:53

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
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='Applicants/uploads/')),
                ('gender', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='Recruiters/uploads/')),
                ('gender', models.CharField(max_length=10)),
                ('company_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('experience', models.IntegerField()),
                ('skills', models.CharField(max_length=100)),
                ('vacancies', models.IntegerField()),
                ('type', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now=True)),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ojp.Recruiter')),
            ],
        ),
        migrations.CreateModel(
            name='Applied',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=10)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ojp.Applicant')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ojp.Job')),
            ],
        ),
    ]
