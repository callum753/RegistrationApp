# Generated by Django 4.2.7 on 2023-12-05 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModuleRegisrationSystem', '0004_remove_module_availabity_module_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='course',
            new_name='courses',
        ),
        migrations.AddField(
            model_name='module',
            name='Availbity',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='yes', max_length=100),
        ),
    ]
