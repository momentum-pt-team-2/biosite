# Generated by Django 3.2.6 on 2021-09-02 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='display_name',
            new_name='name',
        ),
    ]