# Generated by Django 4.0.3 on 2022-04-14 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0006_semesterresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='courseCode',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='result',
            name='courseTitle',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='result',
            name='credit',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='result',
            name='grade',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='result',
            name='gradepoint',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.DeleteModel(
            name='semesterresult',
        ),
    ]
