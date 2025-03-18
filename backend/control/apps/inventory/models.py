from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel

class Item(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    unit = models.CharField(max_length=50, default= 'UND')
    
    class Meta:
        ordering = ['id']
        verbose_name = "Ítem"
        verbose_name_plural = "Ítems"