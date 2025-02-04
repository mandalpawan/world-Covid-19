# Generated by Django 3.0.4 on 2020-04-20 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_crona_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=40)),
                ('total_case', models.CharField(max_length=40)),
                ('new_cases', models.CharField(max_length=40)),
                ('total_death', models.CharField(max_length=40)),
                ('new_death', models.CharField(max_length=40)),
                ('total_recovery', models.CharField(max_length=40)),
                ('active_cases', models.CharField(max_length=40)),
                ('serious_critical', models.CharField(max_length=40)),
                ('total_case_perM', models.CharField(max_length=40)),
                ('totalDeathperM', models.CharField(max_length=40)),
                ('total_test_perM', models.CharField(max_length=40)),
                ('test_perM', models.CharField(max_length=40)),
                ('continent', models.CharField(max_length=40)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
