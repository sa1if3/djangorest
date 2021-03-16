from rest_framework import viewsets,generics, permissions, serializers
from restapi.models import *
from .serializers import *

from django.contrib import admin
admin.autodiscover()
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class QuoteViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Quote.objects.all().order_by('id')
    serializer_class = QuoteSerializer