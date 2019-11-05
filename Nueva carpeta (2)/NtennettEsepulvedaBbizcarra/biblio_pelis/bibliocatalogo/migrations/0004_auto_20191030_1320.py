# Generated by Django 2.2.6 on 2019-10-30 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliocatalogo', '0003_auto_20191026_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Email usuario', max_length=50),
        ),
    ]
