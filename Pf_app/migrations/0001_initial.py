# Generated by Django 3.0.6 on 2020-05-31 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PinCode_Fetcher',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('officename', models.CharField(max_length=200)),
                ('pincode', models.IntegerField()),
                ('officetype', models.CharField(max_length=50)),
                ('deliverystatus', models.CharField(max_length=50)),
                ('divisionname', models.CharField(max_length=100)),
                ('regionname', models.CharField(max_length=100)),
                ('circlename', models.CharField(max_length=100)),
                ('taluk', models.CharField(max_length=100)),
                ('districtname', models.CharField(max_length=100)),
                ('statename', models.CharField(max_length=100)),
                ('Relatedsuboffice', models.CharField(max_length=100)),
                ('Relatedheadoffice', models.CharField(max_length=100)),
            ],
        ),
    ]