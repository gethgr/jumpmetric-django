# Generated by Django 5.0.2 on 2024-02-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jumpmetric', '0021_alter_trial_type_of_trial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trial',
            name='type_of_trial',
            field=models.CharField(choices=[('-', 'Choose'), ('CMJ', 'Cmj'), ('SJ', 'Sj'), ('ISO', 'Iso'), ('DJ', 'Dj')], default='-', max_length=10),
        ),
    ]
