# Generated by Django 4.1.7 on 2024-01-24 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certifications', '0002_rename_certifications_certification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='cert_expiry_date',
            field=models.CharField(max_length=4),
        ),
    ]