import uuid
from django.shortcuts import redirect, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Link
from .serializers import LinkSerializer
from django_filters.rest_framework import DjangoFilterBackend


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    lookup_field = "shortened"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["email"]

    def get_queryset(self):
        email = self.request.query_params.get("email")
        if email:
            return self.queryset.filter(email=email)
        return self.queryset.none()

    def perform_create(self, serializer):
        custom = self.request.data.get("customShortenedUrl")
        if custom:
            if Link.objects.filter(shortened=custom).exists():
                raise serializer.ValidationError(
                    {"customShortenedUrl": "Already taken."}
                )

            shortened = custom
        else:
            shortened = uuid.uuid4().hex[:8]

            serializer.save(shortened=shortened)


@api_view(["GET"])
def redirect_url(request, shortened):
    link = get_object_or_404(Link, shortened=shortened)
    return redirect(link.long_url)
