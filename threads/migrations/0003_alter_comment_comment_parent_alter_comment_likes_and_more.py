# Generated by Django 4.0.4 on 2022-05-28 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0002_rename_name_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nested_comments', to='threads.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='top_level_comments', to='threads.thread'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
