from django.db import migrations
from django.contrib.gis.db import models

class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='location_lat',
        ),
        migrations.RemoveField(
            model_name='project',
            name='location_lon',
        ),
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.PointField(geography=True, null=True, verbose_name='项目位置'),
        ),
    ]
