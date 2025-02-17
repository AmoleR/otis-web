# Generated by Django 3.0.3 on 2020-04-28 13:50

from django.db import migrations


def change_to_unlock(apps, scheme_editor):
    UnitInquiry = apps.get_model("roster", "UnitInquiry")
    UnitInquiry.objects.filter(action_type="ADD").update(action_type="UNLOCK")
    UnitInquiry.objects.filter(action_type="JUMP").update(action_type="UNLOCK")


def change_to_add(apps, scheme_editor):
    UnitInquiry = apps.get_model("roster", "UnitInquiry")
    UnitInquiry.objects.filter(action_type="UNLOCK").update(action_type="ADD")


class Migration(migrations.Migration):
    dependencies = [
        ("roster", "0041_auto_20200428_0950"),
    ]

    operations = [migrations.RunPython(change_to_unlock, change_to_add)]


# vim: expandtab
