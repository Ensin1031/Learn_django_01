# Generated by Django 4.0.2 on 2022-02-25 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_categorydb_alter_newsdb_title_newsdb_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsdb',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.categorydb', verbose_name='Категория'),
        ),
    ]
