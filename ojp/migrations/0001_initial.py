# Generated by Django 2.2.13 on 2023-03-06 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobseeker',
            fields=[
                ('jobseeker_id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('jobseeker_username', models.CharField(default='abc', max_length=50)),
                ('jobseeker_name', models.CharField(max_length=50, null=True)),
                ('jobseeker_email', models.CharField(default='default', max_length=50)),
                ('jobseeker_password', models.CharField(default='default', max_length=50)),
                ('jobseeker_phone', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('recruiter_id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('recruiter_username', models.CharField(default='abc', max_length=50)),
                ('recruiter_name', models.CharField(max_length=50, null=True)),
                ('recruiter_email', models.CharField(default='default', max_length=50)),
                ('recruiter_password', models.CharField(default='default', max_length=50)),
                ('recruiter_phone', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50, null=True)),
                ('education', models.CharField(max_length=50, null=True)),
                ('experience', models.CharField(max_length=50, null=True)),
                ('skills', models.CharField(max_length=50, null=True)),
                ('resume', models.FileField(null=True, upload_to='resume/')),
                ('jobseeker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ojp.Jobseeker')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('job_title', models.CharField(max_length=50, null=True)),
                ('job_description', models.CharField(max_length=50, null=True)),
                ('job_salary', models.CharField(max_length=50, null=True)),
                ('job_type', models.CharField(max_length=50, null=True)),
                ('job_category', models.CharField(max_length=50, null=True)),
                ('job_recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ojp.Recruiter')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedJob',
            fields=[
                ('applied_job_id', models.AutoField(primary_key=True, serialize=False)),
                ('applied_job_status', models.CharField(max_length=50, null=True)),
                ('applied_jobseeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ojp.Jobseeker')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ojp.Job')),
            ],
        ),
    ]
