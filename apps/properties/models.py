from email.policy import default
from django.db import models

import random
import string 
from autoslug import  AutoSlugField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries import CountryField
from apps.common.models import TimeStampedUUIDModel

User = get_user_model

class PropertyPublishedManager(models.Manager):
  def get_queryset(self):
    return(
      super(PropertyPublishedManager, self).get_queryset().filter(published_status=True)
    )
    
class Property(TimeStampedUUIDModel):
  class AdvertType(models.TextChoices):
    FOR_SALE = "For Sale", _("For Sale")
    FOR_RENT = "For Rent", _("For Rent")
    AUCTION = "Auction", _("Auction")
  class PropertyType(models.TextChoices):
    HOUSE="House", _("House")
    APARTMENT = "Appartment", _("Appartment")
    OFFICE ="Office", _("Office")
    WAREHOUSE = "Warehouse", _("Warehouse")
    COMMERCIAL = "Commercial", _("Commercial")
    OTHER = "Other", _("Commercial")
    
  user = models.ForeignKey(User, verbose_name="Aent, Seller, Buyer", related_name="agent_buyer", on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=250, verbose_name=_("Property Title"))
  slug=AutoSlugField(populate_from="title", unique=True, always_update=True)
  ref_code = models.CharField(verbose_name=_("Property Reference code", max_length=225, unique=True, blank=True))
  description=models.TextField(default=_("Default Description"), default=_("Default description...update me please ..."))
  country=CountryField(verbose_name=_("country"), default="UG", blank_label="(select Country")
  
  
  

