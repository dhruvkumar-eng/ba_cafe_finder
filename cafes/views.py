from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Cafe
from .models import Barrio
from .models import Reviewer
from .serializer import CafeSerializer
from .serializer import BarrioSerializer
from .serializer import ReviewerSerializer

class CafeViewSet(viewsets.ReadOnlyModelViewSet):
        # 1. queryset: Defines the collection of objects that this
        #    viewset will operate on. We'll get all cafes, ordered by rating.

        # 2. serializer_class: Tells the viewset which serializer to use
        #    when converting the Cafe objects to JSON.
        queryset = Cafe.objects.all().order_by('-rating')
        serializer_class = CafeSerializer
         # adjust lookup once you confirm the field
            


class BarrioViewSet(viewsets.ReadOnlyModelViewSet):
        # 1. queryset: Defines the collection of objects that this
        #    viewset will operate on. We'll get all cafes, ordered by rating.
        queryset = Barrio.objects.all().order_by('name')
        
        # 2. serializer_class: Tells the viewset which serializer to use
        #    when converting the Cafe objects to JSON.
        serializer_class = BarrioSerializer

class ReviewerViewSet(viewsets.ReadOnlyModelViewSet):
        # 1. queryset: Defines the collection of objects that this
        #    viewset will operate on. We'll get all cafes, ordered by rating.
        queryset = Reviewer.objects.all().order_by('name')
        
        # 2. serializer_class: Tells the viewset which serializer to use
        #    when converting the Cafe objects to JSON.
        serializer_class = ReviewerSerializer