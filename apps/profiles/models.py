from email.policy import default
from django.db import models

from django.contrib.auth import get_user_model
from django.forms import IntegerField
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Gender(models.TextChoices):
  MALE = "Male", _("Male")
  FEMALE = "Female",_("Female")
  OTHER = "Other",_("Other")
  
class Profile(TimeStampedUUIDModel):
  user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
  phone_number = PhoneNumberField(verbose_name=_("Phone Number"), default="+2567516127912", max_length=30)
  about_me = models.TextField(verbose_name="About Me", default="Say something about yourself")
  profile_photo = models.ImageField(verbose_name=_("Profile Photo"),default="/profile_default.png")
  gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices, default=Gender.OTHER, max_length=30)
  country = CountryField(verbose_name=_("Country"), default="UG", blank=False, null=False)
  city = models.CharField(verbose_name=_("City"),max_length=50, default="Kampala",blank=False, null=False)
  license = models.CharField(verbose_name=_("Real Estate License"),max_length=20, blank=True, null=True)
  is_buyer = models.BooleanField(verbose_name=_("Buyer"), help_text=_("Are you looking to Buy a Property?"), default=False)
  is_seller = models.BooleanField(verbose_name=_("Seller"), help_text=_("Are you looking to Sell a Property?"), default=False)
  is_agent = models.BooleanField(verbose_name=_("Agent"), help_text=_("Are you an Agent?"), default=False)
  top_agent = models.BooleanField(verbose_name=_("Top Agent"), default=False)
  rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
  num_reviews =models.IntegerField(verbose_name=_("Number of Reviews"), default=0, null=True, blank=True)
  
  def __str__(self):
    return f"{self.user.username}'s profile"
  
  
  
