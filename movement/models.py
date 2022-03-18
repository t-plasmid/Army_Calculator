from django.db import models
from django.conf import settings
from django.urls import reverse

# pip install misaka
# import misaka

ROUTE_CHOICES = [
    ('Motorway', 'Motorways'),
    ('Urban', 'Urban Roads'),
    ('None', 'Not Specified'),
]

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Route_Type(models.Model):
    route_type = models.CharField(max_length=20, null=False, blank=False)
    acronym = models.CharField(max_length=20, null=True, blank=False)

    def __str__(self):
        return self.acronym


class Brigade(models.Model):
    brigade = models.CharField(max_length=50, null=False, blank=False)
    acronym = models.CharField(max_length=20, null=True, blank=False)

    def __str__(self):
        return self.acronym

    def get_update_url(self):
        return reverse(
            "movement:update_brigade",
            kwargs={
                "pk": self.pk,
            }
        )

    def get_delete_url(self):
        return reverse(
            "movement:delete_brigade",
            kwargs={
                "pk": self.pk,
            }
        )


class Movement_Data(models.Model):
    route_name = models.CharField(max_length=250, null=False, blank=False)
    exercise_name = models.CharField(max_length=100, null=False, blank=False)
    serial = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_time = models.TimeField(null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    speed = models.PositiveIntegerField(null=True, blank=False)
    traffic_density = models.PositiveIntegerField(null=False, blank=False)
    packet_gap = models.PositiveIntegerField(null=True, blank=True)
    unit_gap = models.PositiveIntegerField(null=True, blank=True)
    packet_size = models.PositiveIntegerField(null=True, blank=True)
    route_type = models.ForeignKey(Route_Type, related_name="movement_data", on_delete=models.PROTECT)
    # route_type = models.TextField(choices = ROUTE_CHOICES)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="movement_data", on_delete=models.PROTECT)
    brigade = models.ForeignKey(Brigade, related_name="movement_data", on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id) + " - " + self.route_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "movement:movement_single",
            kwargs={
                "brigade": self.brigade,
                "pk": self.pk,
            }
        )

    def get_update_url(self):
        return reverse(
            "movement:update_movement_plan",
            kwargs={
                "pk": self.pk,
            }
        )

    def get_delete_url(self):
        return reverse(
            "movement:delete_movement_plan",
            kwargs={
                "pk": self.pk,
            }
        )

    class Meta:
        ordering = ["-created_at"]
        # contraints = [
        #     models.UniqueConstraint(fields=['created_by', 'exercise_name', 'pk'], name ='created_exercise_pk')
        # ]


class Unit(models.Model):
    unit = models.CharField(max_length=50, null=False, blank=False)
    acronym = models.CharField(max_length=20, null=True, blank=False)

    def __str__(self):
        return self.acronym

    def get_update_url(self):
        return reverse(
            "movement:update_unit",
            kwargs={
                "pk": self.pk,
            }
        )

    def get_delete_url(self):
        return reverse(
            "movement:delete_unit",
            kwargs={
                "pk": self.pk,
            }
        )


class CP_Detail(models.Model):
    m_id = models.ForeignKey(Movement_Data, related_name="cp_detail", on_delete=models.CASCADE)
    cp_no = models.PositiveIntegerField(null=False, blank=False)
    distance = models.FloatField(null=False, blank=False)
    halt_time = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.m_id) + " - CP" + str(self.cp_no)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_update_url(self):
        return reverse(
            "movement:update_cp_detail",
            kwargs={
                "pk": self.pk,
            }
        )

    def get_delete_url(self):
        return reverse(
            "movement:delete_cp_detail",
            kwargs={
                "pk": self.pk,
            }
        )

    class Meta:
        ordering = ["id"]


class Unit_Detail(models.Model):
    m_id = models.ForeignKey(Movement_Data, related_name="unit_detail", on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, related_name="unit_detail", on_delete=models.PROTECT)
    packet_no = models.PositiveIntegerField(null=False, blank=False)
    vehicle_qty = models.PositiveIntegerField(null=False, blank=False)
    packet_allocated = models.BooleanField(null=False, blank=False, default=False)
    packet_auto_populted = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return str(self.m_id) + " - " + str(self.unit)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "movement:unit_single",
            kwargs={
                "unit": self.unit,
                "pk": self.pk,
                "brigade": self.m_id.brigade
            }
        )

    def get_update_url(self):
        return reverse(
            "movement:update_unit_detail",
            kwargs={
                "pk": self.pk,
            }
        )

    def get_delete_url(self):
        return reverse(
            "movement:delete_unit_detail",
            kwargs={
                "pk": self.pk,
            }
        )

    class Meta:
        ordering = ["id"]


class Packet_Detail(models.Model):
    u_id = models.ForeignKey(Unit_Detail, related_name="packet_detail", on_delete=models.CASCADE)
    subunit = models.CharField(max_length=50, null=False, blank=False)
    packet_no = models.PositiveIntegerField(null=False, blank=False)
    vehicle_qty = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.u_id.m_id) + " - " + str(self.u_id.unit) + " - " + self.subunit

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_update_url(self):
        return reverse(
            "movement:update_packet_detail",
            kwargs={
                "pk": self.pk,
            }
        )

    def get_delete_url(self):
        return reverse(
            "movement:delete_packet_detail",
            kwargs={
                "pk": self.pk,
            }
        )

    class Meta:
        ordering = ["id"]
