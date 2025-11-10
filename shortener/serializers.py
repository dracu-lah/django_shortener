from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    custom = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = Link
        fields = ["shortened", "long_url", "email", "created", "updated", "custom"]
        read_only_fields = ["shortened", "created", "updated"]

        def validate_long_url(self, value):
            if not value.startswith(("http://", "https://")):
                raise serializers.ValidationError("URL must include scheme.")
            return value
