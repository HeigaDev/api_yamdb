# Generated by Django 3.2 on 2023-05-20 21:54

from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[reviews.validators.email_validate], verbose_name='Адрес электронной почты'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, null=True, unique=True, validators=[reviews.validators.username_validate], verbose_name='Имя пользователя'),
        ),
    ]
