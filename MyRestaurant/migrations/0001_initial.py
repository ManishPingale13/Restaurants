# Generated by Django 4.1.1 on 2022-09-19 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menu",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("price", models.IntegerField()),
            ],
        ),
    ]
