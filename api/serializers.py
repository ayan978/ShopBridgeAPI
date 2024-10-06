from importlib.resources import read_binary
from itertools import product
from django.db import transaction
from rest_framework import serializers
from  storeapp.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category_id", "title", "slug"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ "id", "name", "description", "category", "slug", "inventory", "price"]
    
    category = CategorySerializer()