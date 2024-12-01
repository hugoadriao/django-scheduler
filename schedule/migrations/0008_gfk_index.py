from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("schedule", "0007_merge_text_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calendarrelation",
            name="object_id",
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name="eventrelation",
            name="object_id",
            field=models.IntegerField(db_index=True),
        ),
        migrations.AddIndex(
            model_name="calendarrelation",
            index=models.Index(
                fields=["content_type", "object_id"],
                name="calendarrelation_content_type_object_id_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="eventrelation",
            index=models.Index(
                fields=["content_type", "object_id"],
                name="eventrelation_content_type_object_id_idx",
            ),
        ),
        migrations.AlterField(
            model_name="calendar",
            name="slug",
            field=models.SlugField(verbose_name="slug", max_length=200, unique=True),
        ),
    ]
