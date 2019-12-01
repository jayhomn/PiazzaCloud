# Generated by Django 2.2.7 on 2019-12-01 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0004_auto_20191130_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='listCourses',
            field=models.ManyToManyField(to='restAPI.CourseName'),
        ),
    ]
