# Generated by Django 3.2.15 on 2022-11-13 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookExchange', '0011_alter_textbooks_course_alter_textbooks_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='textbooks',
            name='isbn',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
