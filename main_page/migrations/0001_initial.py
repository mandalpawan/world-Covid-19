# Generated by Django 3.0.4 on 2020-04-17 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=40)),
                ('confirm', models.CharField(max_length=40)),
                ('decresed', models.CharField(max_length=40)),
                ('recovered', models.CharField(max_length=40)),
                ('serious', models.CharField(max_length=40)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='update_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.BooleanField()),
                ('improvement', models.BooleanField()),
                ('fix', models.BooleanField()),
                ('subheader', models.CharField(max_length=40)),
                ('content', models.TextField()),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
