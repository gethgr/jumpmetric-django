# Generated by Django 5.0.2 on 2024-02-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jumpmetric', '0011_alter_trial_trial_csv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trial',
            name='trial_csv',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
