# Generated by Django 3.1.4 on 2020-12-06 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201205_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Hey there Check my new Post', max_length=50),
        ),
    ]
