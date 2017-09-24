# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CourseRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Course_Title', models.CharField(unique=True, max_length=50)),
                ('Course_Code', models.CharField(unique=True, max_length=10)),
                ('Course_Unit', models.PositiveSmallIntegerField()),
                ('Semester', models.CharField(choices=[('First_Semester', 'First_Semester'), ('Second_Semester', 'Second_Semester')], max_length=20, default='Select_Semester')),
                ('level', models.ForeignKey(to='Qbank.ClassLevel')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionBank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CourseTitle', models.CharField(max_length=50)),
                ('CourseCode', models.CharField(max_length=10)),
                ('CourseUnit', models.IntegerField()),
                ('Semester', models.CharField(choices=[('First_Semester', 'First_Semester'), ('Second_Semester', 'Second_Semester')], max_length=20, default='Select_Semester')),
                ('Date', models.DateField()),
                ('question_papers', models.FileField(upload_to='QuestionPapers')),
                ('level', models.ForeignKey(to='Qbank.ClassLevel')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Account_Type', models.CharField(choices=[('L', 'Lecturer'), ('S', 'Student')], max_length=1, default='S')),
                ('Upload_Picture', models.ImageField(upload_to='profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
