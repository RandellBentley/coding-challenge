from django.db import models

# Create your models here.

class WebSite(models.Model):
    link_title = models.CharField(max_length=200, unique=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.link_title
