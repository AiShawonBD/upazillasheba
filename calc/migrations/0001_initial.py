# Generated by Django 2.2.7 on 2019-11-26 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory', models.CharField(max_length=100)),
                ('complain', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='Generalpeople',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('district', models.CharField(max_length=100)),
                ('upozilla', models.CharField(max_length=100)),
                ('union', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=100)),
            ],
        ),
    ]
