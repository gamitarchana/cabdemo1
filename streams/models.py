from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet

class LocationTag(models.Model):
    tag = models.CharField(max_length=100, blank=False, null=False, help_text="location tag")

    panels = [
                FieldPanel("tag"),
            ]

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = "Location Tag"
        verbose_name_plural = "Location Tags"

register_snippet(LocationTag)

class TripType(models.Model):
    trip_type = models.CharField(max_length=100, blank=False, null=False, help_text="location tag")

    panels = [
                FieldPanel("trip_type"),
            ]

    def __str__(self):
        return self.trip_type

    class Meta:
        verbose_name = "Trip Type"
        verbose_name_plural = "Trip Types"

register_snippet(TripType)

class FareTable(models.Model):
    AC = 'AC'
    NONAC = 'Non AC'
    FEATURE_CHOICES = (
        (AC, 'AC'),
        (NONAC, 'Non AC'),
    )
    vehicle_type = models.CharField(max_length=100, blank=False, null=False)
    model = models.CharField(max_length=100, blank=False, null=False)
    seater = models.PositiveSmallIntegerField(null=False,default=0)
    per_km_rate = models.PositiveSmallIntegerField(null=False,default=0)
    vehicle_feature = models.CharField(max_length=6,choices=FEATURE_CHOICES, default=AC)

    panels = [
                FieldPanel("vehicle_type"),
                FieldPanel("model"),
                FieldPanel("seater"),
                FieldPanel("per_km_rate"),
                FieldPanel("vehicle_feature"),
            ]

    def __str__(self):
        return self.vehicle_type

    class Meta:
        verbose_name = "Fare"
        verbose_name_plural = "Fares"

register_snippet(FareTable)
