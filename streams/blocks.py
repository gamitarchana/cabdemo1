from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from modelcluster.fields import ParentalKey
from . import constants
from . import models

class PlaceDetailBlock(blocks.StructBlock):
     place = blocks.CharBlock(requried=True)
     details = blocks.TextBlock(requried=True, help_text="Add place details")
     duration_of_visit = blocks.CharBlock(requried=True)
     distance_from_start_location = blocks.IntegerBlock(null=False,default=0)

     map_icon = blocks.StructBlock(
        [
            ("map_icon", ImageChooserBlock(required=False)),
        ]
     )
     trip_types = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("trip_type", SnippetChooserBlock(models.TripType)),
            ]
        )
     )

     tags = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("tag", SnippetChooserBlock(models.LocationTag)),
            ]
        )
     )
     images = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
            ]
        )
     )


     amenities = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("amenity_type", blocks.ChoiceBlock(required=False, max_length=6, choices=constants.AMENITIES_CHOICES)),
                ("location", blocks.CharBlock(required=False)),
            ]
        )
     )

     class Meta:
        template="outstation/place_detail.html"
        icon="edit"
