# Generated by Django 4.2.2 on 2023-06-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapi', '0003_alter_foods_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSignup',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
