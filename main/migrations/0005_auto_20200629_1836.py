<<<<<<< HEAD
# Generated by Django 3.0.7 on 2020-06-29 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200629_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='blog_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='code',
            old_name='code_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='code',
            old_name='code_title',
            new_name='title',
        ),
    ]
=======
# Generated by Django 3.0.7 on 2020-06-29 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200629_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='blog_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='code',
            old_name='code_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='code',
            old_name='code_title',
            new_name='title',
        ),
    ]
>>>>>>> bc1000db8c48c1e68896bc37fe6e054a1877830a
