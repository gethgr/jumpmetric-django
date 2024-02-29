# Generated by Django 5.0.2 on 2024-02-11 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jumpmetric', '0004_alter_trial_trial_csv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trial',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trial',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trial',
            name='occupy',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trial',
            name='trial_csv',
            field=models.FileField(blank=True, null=True, upload_to='trials_csv/'),
        ),
        migrations.AlterField(
            model_name='trial',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
