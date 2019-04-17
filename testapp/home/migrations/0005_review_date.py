# Generated by Django 2.0.13 on 2019-04-01 12:32

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.blocks.field_block
import wagtail.core.fields
import wagtail.images.blocks
import wagtailnhsukfrontend.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_paginationpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='last_review_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='next_review_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True))])), ('care_card', wagtail.core.blocks.StructBlock([('type', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('urgent', 'Urgent'), ('immediate', 'Immediate')])), ('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('details', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('do_list', wagtail.core.blocks.StructBlock([('do', wagtail.core.blocks.ListBlock(wagtail.core.blocks.field_block.RichTextBlock))])), ('dont_list', wagtail.core.blocks.StructBlock([('dont', wagtail.core.blocks.ListBlock(wagtail.core.blocks.field_block.RichTextBlock))])), ('expander', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('expander_group', wagtail.core.blocks.StructBlock([('expanders', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.ExpanderBlock))])), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('panel', wagtail.core.blocks.StructBlock([('labeled_title', wagtail.core.blocks.CharBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))]))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='external URL', required=True)), ('newWindow', wagtail.core.blocks.BooleanBlock())])), ('care_card', wagtail.core.blocks.StructBlock([('type', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('urgent', 'Urgent'), ('immediate', 'Immediate')])), ('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('details', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('expander', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('expander_group', wagtail.core.blocks.StructBlock([('expanders', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.ExpanderBlock))])), ('inset_text', wagtailnhsukfrontend.blocks.InsetTextBlock()), ('panel', wagtail.core.blocks.StructBlock([('labeled_title', wagtail.core.blocks.CharBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtailnhsukfrontend.blocks.WarningCalloutBlock())]),
        ),
         migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('newWindow', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))])), ('care_card', wagtail.core.blocks.StructBlock([('type', wagtail.core.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('urgent', 'Urgent'), ('immediate', 'Immediate')])), ('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('details', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('do_list', wagtail.core.blocks.StructBlock([('do', wagtail.core.blocks.ListBlock(wagtail.core.blocks.field_block.RichTextBlock))])), ('dont_list', wagtail.core.blocks.StructBlock([('dont', wagtail.core.blocks.ListBlock(wagtail.core.blocks.field_block.RichTextBlock))])), ('expander', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('expander_group', wagtail.core.blocks.StructBlock([('expanders', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.ExpanderBlock))])), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('panel', wagtail.core.blocks.StructBlock([('labeled_title', wagtail.core.blocks.CharBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))]))]),
        ),
    ]
