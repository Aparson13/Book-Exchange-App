# Generated by Django 3.2.15 on 2022-11-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookExchange', '0007_textbooks_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(blank=True, null=True, related_name='favorited_by', to='BookExchange.Textbooks'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(choices=[('On Grounds', 'On Grounds'), ('Off Grounds', 'Off Grounds')], default='On Grounds', max_length=15),
        ),
    ]
