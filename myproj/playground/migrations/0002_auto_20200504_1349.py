# Generated by Django 3.0.5 on 2020-05-04 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinformation',
            name='pass_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
