from rest_framework import serializers
from .models import WebSite

class WebSiteSerializer(serializers.ModelSerializer):
  class Meta:
    model = WebSite
