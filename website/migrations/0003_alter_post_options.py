# Generated by Django 4.2.9 on 2024-05-08 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
    ]