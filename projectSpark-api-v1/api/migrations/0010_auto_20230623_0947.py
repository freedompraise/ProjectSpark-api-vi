# Generated by Django 3.2 on 2023-06-23 09:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0009_idea_aveerage_rating"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="idearating",
            name="rating",
        ),
        migrations.AddField(
            model_name="idearating",
            name="value",
            field=models.SmallIntegerField(
                choices=[(1, "Upvote"), (-1, "Downvote"), (0, "Neutral")], default=0
            ),
        ),
    ]
