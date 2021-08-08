from rest_framework import serializers

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


class ShopUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUser
        fields = '__all__'

        read_only_fields = ['id', 'password', 'email']

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.username = validated_data['username']
        instance.last_name = validated_data['last_name']
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
