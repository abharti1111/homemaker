from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _


# account serializers here
class userCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        required=True, 
         
        style={'input_type':'password'}
        )
    password2 = serializers.CharField(
        write_only=True, 
        required=True, 
         
        style={'input_type':'password'}
        )
        


    class Meta:
        model = User
        fields = ['email','password','first_name','last_name','password2']
        extra_kwargs = {'password':{'write_only':True}}
        read_only_fields = ['username']

    def validate(self, data):
        pw = data['password']
        pw2 = data['password2']
        if pw != pw2:
            raise serializers.ValidationError('passwords must match')
        return data

    def create(self,validated_data):
        # print(validated_data)
        user = User(
            email=validated_data['email'],
            username = validated_data['email'].split("@")[0],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        
        user.set_password(validated_data['password'])
        user.save()
        return user

class authTokenSerializer(serializers.Serializer):
    username = serializers.CharField(label=_("username/email"))
    password = serializers.CharField(label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']
        if username and password:
            try:
                username = User.objects.get(
                    Q(username__iexact=username)|
                    Q(email__iexact=username)
                )
                print(username)
                user = authenticate(request=self.context['request'],username=username,password=password)
                print(user)
                if not user:
                    msg = _('Unable to log in with provided credentials.')
                    raise serializers.ValidationError(msg, code='authorization')
            except:

                print(username)
                user = authenticate(request=self.context['request'],username=username,password=password)
                print(user)
                if not user:
                    msg = _('Unable to log in with provided credentials.')
                    raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
                
# class userAddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fields = ['flatNo','street','landmark','city','district','state','pinCode']

class userProfileUpdateSerializer(serializers.ModelSerializer):
    # address = userCreateSerializer(many=True,read_only=True)
    # address = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Address.objects.all())
    class Meta:
        model = Profile
        fields = ['user','phoneNumber','profilePicture','userType','flatNo','street','landmark','city','district','state','pinCode']



#     def create(self, validated_data):
#         address_data = validated_data.pop('address')
#         userProfile = Profile.objects.create(**validated_data)
#         # print(address_data,userProfile)
#         for ad in address_data:
#             Address.objects.create(user=userProfile,**validated_data)
#         return userProfile
#     def update(self, instance, validated_data):
#         address_data = validated_data.pop('address')
#         print(instance.address)
#         addresses = list((instance.address).all())

#         instance.user = validated_data.get('user',instance.user)
#         instance.phoneNumber = validated_data.get('user',instance.phoneNumber)
#         instance.profilePicture = validated_data.get('user',instance.profilePicture)
#         instance.userType = validated_data.get('user',instance.userType)
#         instance.save()

#         for ad in address_data:
#             addr = addresses.pop(0)
#             adddr.flatNo = ad.get('flatNo',adddr.flatNo)
#             adddr.street = ad.get('street',adddr.street)
#             adddr.landmark = ad.get('landmark',adddr.landmark)
#             adddr.city = ad.get('city',adddr.city)
#             adddr.district = ad.get('district',adddr.district)
#             adddr.state = ad.get('state',adddr.state)
#             adddr.pinCode = ad.get('pinCode',adddr.pinCode)
#             addr.save()
#         return instance
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     print(data['address'][0])
    #     # data['address'] = userAddressSerializer(Address.objects.get(pk=data['address'])).data
    #     return data


        


    

