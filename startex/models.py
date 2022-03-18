from django.db import models
from django.urls import reverse
import movement.models as mm

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class StartEx_Plan(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    brigade = models.ForeignKey(mm.Brigade, related_name="startex_plan", on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="startex_plan", on_delete=models.PROTECT)

    def __str__(self):
        return str(self.pk) + " - " + str(self.name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_detailview_url(self):
        return reverse(
            "startex:detail_startex_plan",
            kwargs={
                "pk": self.pk,
            }
        )

    def get_update_url(self):
        return reverse(
            "startex:update_startex_plan",
            kwargs={
                "pk": self.pk,
            }
        )

    def get_delete_url(self):
        return reverse(
            "startex:delete_startex_plan",
            kwargs={
                "pk": self.pk,
            }
        )

    class Meta:
        ordering = ["-created_at"]


class SX_Vehicle_Data(models.Model):
    VEHICLE_CATEGORY = (
        ('A', 'A'),
        ('B', 'B'),
        ('B+E', 'B+E'),
        ('C', 'C'),
        ('C+E', 'C+E'),
        ('D1', 'D1'),
        ('D', 'D'),
        ('D+E', 'D+E'),
    )
    name = models.CharField(max_length=150, null=False, blank=False)
    model = models.CharField(max_length=250, null=False, blank=False)
    category = models.CharField(max_length=250, null=False, blank=False, choices=VEHICLE_CATEGORY)

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse(
            "startex:update_sx_vehicle_data",
            kwargs={
                "pk": self.pk,
            }
        )

    def get_delete_url(self):
        return reverse(
            "startex:delete_sx_vehicle_data",
            kwargs={
                "pk": self.pk,
            }
        )


class SX_Unit_Detail(models.Model):
    sx_id = models.ForeignKey(StartEx_Plan, related_name="sx_unit_detail", on_delete=models.CASCADE)
    u_id = models.ForeignKey(mm.Unit, related_name="sx_unit_detail", on_delete=models.PROTECT)

    def __str__(self):
        return str(self.sx_id) + " - " + str(self.u_id)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_update_url(self):
        return reverse(
            "startex:update_sx_unit_detail",
            kwargs={
                "pk": self.pk,
            }
        )

    def get_delete_url(self):
        return reverse(
            "startex:delete_sx_unit_detail",
            kwargs={
                "pk": self.pk,
            }
        )

    class Meta:
        ordering = ["id"]


class SX_Vehicle_Detail(models.Model):
    sx_u_id = models.ForeignKey(SX_Unit_Detail, related_name="sx_vehicle_detail", on_delete=models.CASCADE)
    sx_v_id = models.ForeignKey(SX_Vehicle_Data, related_name="sx_vehicle_detail", on_delete=models.PROTECT)
    qty = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.sx_u_id) + " - " + str(self.sx_v_id)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_update_url(self):
        return reverse(
            "startex:update_sx_vehicle_detail",
            kwargs={
                "pk": self.pk,
            }
        )

    def get_delete_url(self):
        return reverse(
            "startex:delete_sx_vehicle_detail",
            kwargs={
                "pk": self.pk,
            }
        )

    class Meta:
        ordering = ["id"]
