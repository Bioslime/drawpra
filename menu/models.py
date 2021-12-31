from django.db import models
from django.db.models.deletion import CASCADE
import uuid
from django.utils import timezone

import sys
sys.path.append("../")
from accounts.models import CustomUser

# Create your models here.

class PictData(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    picture = models.ImageField()
    url = models.URLField(blank=False, null=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)


class GoodPoint(models.Model):
    pict = models.ForeignKey(PictData, on_delete=CASCADE)
    text = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class DetailGoodPoint(models.Model):
    goopo = models.ForeignKey(GoodPoint, on_delete=CASCADE)
    text = models.TextField()
    clear_check = models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)