# Generated by Django 3.0.5 on 2020-05-05 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0007_auto_20200505_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
