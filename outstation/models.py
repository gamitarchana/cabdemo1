from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
    MultiFieldPanel,
    InlinePanel,
)
from wagtail.api import APIField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from modelcluster.fields import ParentalKey
#from django.core import serializer
from django.conf import settings
from django.contrib.auth.models import User

from streams import blocks
from streams import constants
from streams.models import LocationTag, TripType, FareTable


# Create your models here.

class OutstationRoutePage(Page):
    template="outstation/outstation_route_page.html"

    banner_title=models.CharField(max_length=100, null=False)
    banner_image=models.ForeignKey(
        "wagtailimages.Image",
        null=False,
        on_delete=models.CASCADE,
        related_name="+")

    start_location = models.CharField(max_length=100, null=False)
    start_location_details = models.TextField(null=False, help_text="Add start location details")
    start_location_map_icon = models.ForeignKey(
        "wagtailimages.Image",
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="+")
    destination = models.CharField(max_length=100, null=False)
    destination_details = models.TextField(null=False, help_text="Add destination details")
    destination_map_icon = models.ForeignKey(
        "wagtailimages.Image",
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="+")

    tourist_places_on_route = StreamField(
         [
            ("tourist_location", blocks.PlaceDetailBlock()),
        ],
        null=True,
        blank=True
    )

    tourist_places_in_destination = StreamField(
         [
            ("tourist_location", blocks.PlaceDetailBlock()),
        ],
        null=True,
        blank=True
    )

    road_condition_rating = models.PositiveSmallIntegerField()
    road_map = models.TextField(null=False, help_text="Add road map details")
    best_time_to_visit = models.TextField(null=False, help_text="Add road map details")
    alternate_routes = models.TextField(null=False, help_text="Add alternate route details")
    road_condition = models.TextField(null=False, help_text="Add road condition details")

    total_distance = models.PositiveSmallIntegerField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    api_fields = [
        APIField("banner_title"),
        APIField("banner_image"),
        APIField("start_location"),
        APIField("start_location_details"),
        APIField("start_location_images"),
        APIField("start_location_map_icon"),
        APIField("destination"),
        APIField("destination_details"),
        APIField("destination_images"),
        APIField("destination_map_icon"),
        APIField("tourist_places_on_route"),
        APIField("tourist_places_in_destination"),
        APIField("road_condition_rating"),
        APIField("road_map"),
        APIField("best_time_to_visit"),
        APIField("alternate_routes"),
        APIField("road_condition"),
        APIField("total_distance"),
    ]

    content_panels = Page.content_panels+ [
        FieldPanel("banner_title"),
        ImageChooserPanel("banner_image"),
        FieldPanel("start_location"),
        FieldPanel("start_location_details"),
        MultiFieldPanel([
            InlinePanel("start_location_images"),
        ], heading="Start Location Images" ),
        ImageChooserPanel("start_location_map_icon"),
        FieldPanel("destination"),
        FieldPanel("destination_details"),
        MultiFieldPanel([
            InlinePanel("destination_images"),
        ], heading="Destination Images" ),
        ImageChooserPanel("destination_map_icon"),
        StreamFieldPanel("tourist_places_on_route"),
        StreamFieldPanel("tourist_places_in_destination"),
        FieldPanel("road_condition_rating"),
        FieldPanel("road_map"),
        FieldPanel("best_time_to_visit"),
        FieldPanel("alternate_routes"),
        FieldPanel("road_condition"),
        FieldPanel("total_distance"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        location_tags = LocationTag.objects.all()
        context["location_tags"] = location_tags

        trip_types = TripType.objects.all()
        context["trip_types"] = trip_types

        fare_table = FareTable.objects.all()
        context["fare_table"] = fare_table

        context["total_likes"] = self.total_likes()

        context["total_reviews"] = self.total_reviews()

        context["AMENITIES"] = constants.AMENITIES

        context["data_api"] = settings.REST_API_ENDPOINT

        return context

    def total_likes(self):
        return self.likes.count()

    def total_reviews(self):
        return self.page_review.count()

class StartLocationImages(Orderable):
    page = ParentalKey("outstation.OutstationRoutePage", related_name="start_location_images", null=False, blank=False)
    start_location_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True, blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    panels = [
        ImageChooserPanel("start_location_image"),
    ]

class DestinationImages(Orderable):
    page = ParentalKey("outstation.OutstationRoutePage", related_name="destination_images", null=False, blank=False)
    destination_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True, blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    panels = [
        ImageChooserPanel("destination_image"),
    ]
