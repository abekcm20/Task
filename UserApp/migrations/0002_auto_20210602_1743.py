# Generated by Django 3.0 on 2021-06-02 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='task_pic',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='static'),
        ),
    ]
