# Generated by Django 2.2.7 on 2020-05-16 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='add_amount',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='due_amount',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='paid_amount',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='total_amount',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
