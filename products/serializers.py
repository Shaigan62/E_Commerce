from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Image
        fields = '__all__'

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Variant
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Rating
        fields = '__all__'

class ProductDetailsSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    variants = ProductVariantSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
        extra_fields = ['images']
        depth = 3

class ProductByCategorySeializer(serializers.ModelSerializer):
    pro_category = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = '__all__'
        extra_fields=['pro_category']
        depth = 3



