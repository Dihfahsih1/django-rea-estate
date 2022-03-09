from django.contrib.auth import get_user_model
from numpy import source
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreationSerializer
from phonenumber_field.serializersfields import PhoneNumberField
from rest_framework import serializers

User = get_user_model

class UserSerializer(serializers.ModelSerializer):
  gender = serializers.CharField(source="profile.gender")
  phone_number= PhoneNumberField(source="profile.phone_number")
  profile_photo = serializers.ImageField(source="profile.profile_photo")
  country = CountryField(source="profile.country",)
  city = serializers.CharField(source="profile.city")
  top_seller = serializers.BooleanField(source="profile.top_seller")
  first_name = serializers.SerializerMethodField()
  last_name = serializers.SerializerMethodField()
  full_name = serializers.SerializerMethodField(source="get_full_name")
  
  class Meta:
    model=User  
    fields = ["id", "username", "email", "first_name", "last_name", "full_name"]
  