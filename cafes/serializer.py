from rest_framework import serializers
from .models import Cafe
from .models import Barrio
from .models import Reviewer  
from .models import Review

# We create a class that inherits from DRF's ModelSerializer.
class CafeSerializer(serializers.ModelSerializer):
        summary = serializers.SerializerMethodField()
        def get_summary(self, obj):
         return f"{obj.name} is a {obj.rating}-star cafe."
        # The Meta class is where we configure the serializer.
        class Meta:
            # 1. Tell the serializer which model it's based on.
            model = Cafe
            # 2. Define the "whitelist" of fields to include in the API.
            fields = ['id', 'name', 'barrio','address', 'rating', 'has_good_medialunas','summary', 'notes']

class BarrioSerializer(serializers.ModelSerializer):
      class Meta:
            # 1. Tell the serializer which model it's based on.
            model = Barrio
            # 2. Define the "whitelist" of fields to include in the API.
            fields = ['id', 'name', 'communa']

class ReviewerSerializer(serializers.ModelSerializer):
      class Meta:
            # 1. Tell the serializer which model it's based on.
            model = Reviewer
            # 2. Define the "whitelist" of fields to include in the API.
            fields = [ 'name', 'join_date']

class ReviewModelSerializer(serializers.ModelSerializer):
      class Meta:
            # 1. Tell the serializer which model it's based on.
            model = Review
            # 2. Define the "whitelist" of fields to include in the API.
            fields = ['id','cafe', 'reviewer', 'comment', 'rating']