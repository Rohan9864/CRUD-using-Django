# Generated by Django 5.1 on 2024-09-02 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Isdelete',
            field=models.BooleanField(default=False),
        ),
    ]
