from django.db import models
from ..accounts.models import CustomUser
import uuid
from django.utils import timezone

# Create your models here.

class PictData(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    picture = models.ImageField()
    url = models.URLField(blank=False, null=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
