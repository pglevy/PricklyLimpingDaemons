# Generated by Django 5.0.2 on 2024-03-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('done', models.BooleanField()),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('doneOn', models.DateTimeField()),
                ('type', models.CharField(choices=[('1', 'Physical'), ('2', 'Digital'), ('3', 'Mental')], max_length=2)),
            ],
        ),
    ]