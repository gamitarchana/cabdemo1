# Generated by Django 2.1.8 on 2019-05-20 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import streams.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailimages', '0001_squashed_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('destination_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OutstationRoutePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('banner_title', models.CharField(max_length=100)),
                ('start_location', models.CharField(max_length=100)),
                ('start_location_details', models.TextField(help_text='Add start location details')),
                ('destination', models.CharField(max_length=100)),
                ('destination_details', models.TextField(help_text='Add destination details')),
                ('tourist_places_on_route', wagtail.core.fields.StreamField([('tourist_location', wagtail.core.blocks.StructBlock([('place', wagtail.core.blocks.CharBlock(requried=True)), ('details', wagtail.core.blocks.TextBlock(help_text='Add place details', requried=True)), ('duration_of_visit', wagtail.core.blocks.CharBlock(requried=True)), ('distance_from_start_location', wagtail.core.blocks.IntegerBlock(default=0, null=False)), ('map_icon', wagtail.core.blocks.StructBlock([('map_icon', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('trip_types', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('trip_type', wagtail.snippets.blocks.SnippetChooserBlock(streams.models.TripType))]))), ('tags', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('tag', wagtail.snippets.blocks.SnippetChooserBlock(streams.models.LocationTag))]))), ('images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])))]))], blank=True, null=True)),
                ('tourist_places_in_destination', wagtail.core.fields.StreamField([('tourist_location', wagtail.core.blocks.StructBlock([('place', wagtail.core.blocks.CharBlock(requried=True)), ('details', wagtail.core.blocks.TextBlock(help_text='Add place details', requried=True)), ('duration_of_visit', wagtail.core.blocks.CharBlock(requried=True)), ('distance_from_start_location', wagtail.core.blocks.IntegerBlock(default=0, null=False)), ('map_icon', wagtail.core.blocks.StructBlock([('map_icon', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('trip_types', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('trip_type', wagtail.snippets.blocks.SnippetChooserBlock(streams.models.TripType))]))), ('tags', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('tag', wagtail.snippets.blocks.SnippetChooserBlock(streams.models.LocationTag))]))), ('images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])))]))], blank=True, null=True)),
                ('road_condition_rating', models.PositiveSmallIntegerField()),
                ('road_map', models.TextField(help_text='Add road map details')),
                ('best_time_to_visit', models.TextField(help_text='Add road map details')),
                ('alternate_routes', models.TextField(help_text='Add alternate route details')),
                ('road_condition', models.TextField(help_text='Add road condition details')),
                ('total_distance', models.PositiveSmallIntegerField()),
                ('banner_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
                ('destination_map_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('start_location_map_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StartLocationImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_location_images', to='outstation.OutstationRoutePage')),
                ('start_location_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='destinationimages',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_images', to='outstation.OutstationRoutePage'),
        ),
    ]
