# Generated by Django 2.2 on 2022-03-15 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioDatabase', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_message',
            field=models.TextField(max_length=1000),
        ),
    ]
