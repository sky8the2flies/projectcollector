# Generated by Django 3.1.1 on 2020-09-17 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_timeline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('git_user', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
    ]
