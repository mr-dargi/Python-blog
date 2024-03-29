# Generated by Django 4.2.5 on 2023-10-31 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_remove_article_hits"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArticleHit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.article"
                    ),
                ),
                (
                    "ip_address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.ipaddress"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="article",
            name="hits",
            field=models.ManyToManyField(
                blank=True,
                related_name="hits",
                through="blog.ArticleHit",
                to="blog.ipaddress",
                verbose_name="بازدید ها",
            ),
        ),
    ]
