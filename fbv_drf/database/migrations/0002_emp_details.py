# Generated by Django 4.2.2 on 2023-07-24 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('ocp', models.IntegerField()),
                ('post', models.CharField(max_length=250)),
                ('org', models.TextField()),
            ],
        ),
    ]