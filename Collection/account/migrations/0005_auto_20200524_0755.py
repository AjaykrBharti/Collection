# Generated by Django 2.1.15 on 2020-05-24 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200524_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='EmpComp',
            field=models.CharField(choices=[('Tata', 'Tata'), ('EEEHUB', 'EEEHUB'), ('ISRO', 'ISRO')], max_length=10, null=True),
        ),
    ]
