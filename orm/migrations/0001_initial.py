# Generated by Django 4.2.4 on 2023-12-09 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='john', max_length=30)),
                ('last_name', models.CharField(default='doe', max_length=30)),
                ('dob', models.DateField(null=True)),
            ],
        ),
    ]
