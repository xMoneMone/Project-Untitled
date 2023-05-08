# Generated by Django 4.2.1 on 2023-05-08 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='faceit_esportal_esea',
        ),
        migrations.AddField(
            model_name='post',
            name='esea',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='esportal',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='faceit',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='role2',
            field=models.CharField(blank=True, choices=[('IGL', 'IGL'), ('Lurk', 'Lurk'), ('Support', 'Support'), ('Entry', 'Entry'), ('AWP', 'AWP'), ('Secondary AWP', 'Secondary AWP')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='role3',
            field=models.CharField(blank=True, choices=[('IGL', 'IGL'), ('Lurk', 'Lurk'), ('Support', 'Support'), ('Entry', 'Entry'), ('AWP', 'AWP'), ('Secondary AWP', 'Secondary AWP')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='team_experience',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tournament_experience',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
    ]