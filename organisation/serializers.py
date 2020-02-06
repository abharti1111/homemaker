from rest_framework import serializers
from .models import Organisation,Menu

class OrganisationViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = (
            'name',
            'picture',
            'isVeg',
            # 'menu',
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
            # 'menu',
            'weeklyPrice',
            'description',
            'panId',
            'owner',
            'facebook_page',
            'instagram_page',
            'fssai_Lic'
        )
        
        verbose_name = 'Organisation'
        verbose_name_plural = 'Organisations'
class MenuSerializer(serializers.ModelSerializer):
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
            'org',
        )
        
    # def create(self, validated_data):
    #     data = super().create(validated_data)
    #     print(data,self.context['request'].user.profile.organisation)
    #     # validated_data['org'] = self.context['request'].user.profile.organisation
    #     return data
