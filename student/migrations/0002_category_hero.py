# Generated by Django 4.1 on 2022-08-27 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('benevolence_factor', models.PositiveSmallIntegerField(default=50, help_text='How benevolent this hero is?')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.category')),
            ],
        ),
    ]
