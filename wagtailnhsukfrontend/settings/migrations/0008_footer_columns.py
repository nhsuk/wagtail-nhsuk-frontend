# Generated by Django 3.2 on 2024-02-22 15:46

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailnhsukfrontendsettings', '0007_organisational_header'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footerlinks',
            name='setting',
        ),
        migrations.CreateModel(
            name='FooterColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('column_title', models.CharField(blank=True, max_length=250, null=True)),
                ('setting', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='footer_columns', to='wagtailnhsukfrontendsettings.footersettings')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='footerlinks',
            name='column',
            field=modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='footer_links', to='wagtailnhsukfrontendsettings.footercolumn'),
        ),
    ]
