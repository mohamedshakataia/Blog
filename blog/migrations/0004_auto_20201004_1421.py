# Generated by Django 3.1.2 on 2020-10-04 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
    ]
