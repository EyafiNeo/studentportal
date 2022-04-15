# Generated by Django 4.0.3 on 2022-04-14 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0005_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='semesterresult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseTitle', models.CharField(default='', max_length=255)),
                ('courseCode', models.CharField(default='', max_length=255)),
                ('credit', models.CharField(default='', max_length=255)),
                ('grade', models.CharField(default='', max_length=255)),
                ('gradepoint', models.CharField(default='', max_length=255)),
                ('semestername', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semesterresult', to='profileapp.result')),
            ],
        ),
    ]
