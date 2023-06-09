# Generated by Django 4.2 on 2023-05-05 06:07

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('continent', models.CharField(choices=[('ASIA', 'Asia'), ('AFRIC', 'Africa'), ('NA', 'North America'), ('SA', 'South America'), ('ANTIC', 'Antacitica'), ('EURO', 'Europe'), ('AUS', 'Australia')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('level', models.CharField(max_length=255)),
                ('study_field', models.CharField(max_length=255)),
                ('school', models.CharField(max_length=255)),
                ('deadline', models.DateField()),
                ('more_info', models.TextField()),
                ('link_web', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
    ]
