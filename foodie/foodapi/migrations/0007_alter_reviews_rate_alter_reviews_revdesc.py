# Generated by Django 4.2.2 on 2023-06-29 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapi', '0006_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='revdesc',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
