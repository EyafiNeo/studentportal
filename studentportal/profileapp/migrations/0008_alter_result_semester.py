# Generated by Django 4.0.3 on 2022-04-14 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0007_result_coursecode_result_coursetitle_result_credit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='semester',
            field=models.CharField(default='', max_length=255),
        ),
    ]
