# Generated by Django 2.0.1 on 2018-01-10 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ['display_order', 'name']},
        ),
        migrations.AddField(
            model_name='file',
            name='display_order',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]