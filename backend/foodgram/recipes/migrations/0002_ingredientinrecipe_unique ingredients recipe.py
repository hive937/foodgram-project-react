# Generated by Django 3.2.18 on 2023-03-02 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='ingredientinrecipe',
            constraint=models.UniqueConstraint(fields=('ingredient', 'recipe'), name='unique ingredients recipe'),
        ),
    ]
