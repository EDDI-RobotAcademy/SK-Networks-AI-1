from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from travel.entity.models import Travel

# Create your views here.

class TravelView(viewsets.ViewSet):
    queryset = Travel.objects.all()



