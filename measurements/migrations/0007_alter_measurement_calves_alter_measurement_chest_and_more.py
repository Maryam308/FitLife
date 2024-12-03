# Generated by Django 4.1.13 on 2024-12-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "measurements",
            "0006_alter_measurement_calves_alter_measurement_chest_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="measurement",
            name="calves",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="chest",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="hips",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="left_arm",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="right_arm",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="thighs",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="measurement",
            name="waist",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
    ]
