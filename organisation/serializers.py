from rest_framework import serializers
from .models import Organisation,Menu

class OrganisationViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = (
            'name',
            'picture',
            'isVeg',
            'menu',
            'weeklyPrice',
            'description',
        )
        read_only_fields=(
            'panId',
            'owner',
            'ratings',
            'created_at',
        )
        verbose_name = 'Organisation'
        verbose_name_plural = 'Organisations'
class OrganisationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = (
            'name',
            'picture',
            'isVeg',
            'menu',
            'weeklyPrice',
            'description',
            'panId',
        )
        read_only_fields=(
            'owner',
            'ratings',
            'created_at',
        )
        verbose_name = 'Organisation'
        verbose_name_plural = 'Organisations'
class MenuViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields=(
            'sunday',
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
        )
