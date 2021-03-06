# Generated by Django 3.1.1 on 2020-10-19 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0006_auto_20201019_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternative',
            name='qid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alternatives', to='questionnaire.question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='qid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questionnaire.question'),
        ),
        migrations.AlterField(
            model_name='label',
            name='alternatives',
            field=models.ManyToManyField(related_name='labels', to='questionnaire.Alternative'),
        ),
    ]
