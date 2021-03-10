# Generated by Django 3.1.7 on 2021-03-10 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15)),
                ('Contact_email', models.EmailField(max_length=15)),
                ('Address', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
