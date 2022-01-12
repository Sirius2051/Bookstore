# Generated by Django 4.0.1 on 2022-01-12 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('publication_date', models.DateField()),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('isbn', models.TextField(blank=True, null=True)),
            ],
        ),
    ]