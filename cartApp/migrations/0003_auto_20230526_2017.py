from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('cartApp', '0002_auto_20230526_2010'),
    ]

    operations = [
        migrations.RunSQL('DROP TABLE IF EXISTS cartApp;'),
    ]
