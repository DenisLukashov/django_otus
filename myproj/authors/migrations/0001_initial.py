# Generated by Django 3.0.5 on 2020-05-03 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'AuthorsModel',
                'verbose_name_plural': 'AuthorsModels',
            },
        ),
    ]
