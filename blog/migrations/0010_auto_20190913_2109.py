# Generated by Django 2.2.5 on 2019-09-13 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190913_1713'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['published_at'], 'verbose_name': 'комментарий', 'verbose_name_plural': 'комментарии'},
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]