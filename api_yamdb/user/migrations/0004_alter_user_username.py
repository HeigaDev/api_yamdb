# Generated by Django 3.2 on 2023-05-21 14:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20230521_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=150, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+\\Z')], verbose_name='Имя пользователя'),
            preserve_default=False,
        ),
    ]
