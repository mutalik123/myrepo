# Generated by Django 2.1.7 on 2019-03-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20190307_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem1',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
