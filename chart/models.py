from django.db import models
from django.utils import timezone
from product.models import Brand


class Content(models.Model):
    title = models.ForeignKey(Brand, on_delete=models.CASCADE)
    language = models.CharField(max_length=220)
    month_name = models.CharField(max_length=220)
    monthly_active_user = models.PositiveIntegerField()

    global_rank = models.PositiveIntegerField()
    country_traffic = models.CharField(max_length=220)
    social_media_traffic = models.PositiveIntegerField()
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title} - {self.month_name}'