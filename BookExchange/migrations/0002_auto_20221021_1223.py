# Generated by Django 3.2.15 on 2022-10-21 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookExchange', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='textbooks',
            old_name='firstname',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='textbooks',
            old_name='lastname',
            new_name='condition',
        ),
        migrations.AddField(
            model_name='textbooks',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='textbooks',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
