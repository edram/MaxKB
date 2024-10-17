# Generated by Django 4.2.15 on 2024-10-15 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0008_alter_document_status_alter_paragraph_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='status',
            field=models.CharField(choices=[('0', '导入中'), ('1', '已完成'), ('2', '导入失败'), ('3', '排队中'), ('4', '生成问题中')], default='3', max_length=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='status',
            field=models.CharField(choices=[('0', '导入中'), ('1', '已完成'), ('2', '导入失败'), ('3', '排队中'), ('4', '生成问题中')], default='0', max_length=1, verbose_name='状态'),
        ),
    ]