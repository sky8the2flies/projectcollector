# Generated by Django 3.1.1 on 2020-09-17 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_person'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Author',
        ),
        migrations.AddField(
            model_name='project',
            name='authors',
            field=models.ManyToManyField(to='main_app.Author'),
        ),
    ]