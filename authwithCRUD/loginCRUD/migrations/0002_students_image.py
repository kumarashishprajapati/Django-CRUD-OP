# Generated by Django 4.1.2 on 2023-04-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginCRUD', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='image',
            field=models.ImageField(default='', upload_to='static/images'),
        ),
    ]