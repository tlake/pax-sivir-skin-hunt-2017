from django.db import models


class SkinCode(models.Model):
    name = models.CharField(max_length=63, default="")
    code = models.CharField(max_length=63, default="")
    claimed = models.BooleanField(default=False)
    human_name = models.CharField(max_length=63, default="")
    summoner_name = models.CharField(max_length=63, default="")
