# Generated by Django 4.1.1 on 2022-12-27 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0002_rename_question_questions_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
