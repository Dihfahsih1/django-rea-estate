from django.contrib.auth.base_user import  BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import  gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('You must provide a valid email address'))
    
    def create_user(self, email, username, first_name, last_name, password, **extra_fields):
        if not username:
            raise ValueError(_('Users must submit a username'))
        
        if not first_name:
            raise ValueError(_('Uses must submit a first name'))
        
        if not last_name:
            raise ValueError(_('Uses must submit a last name'))
   
        if email:
            email=self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User account: An email address is required"))
        
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )
        
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, password, first_name, last_name,email, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_actve", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValidationError(_("superusers must have is_staff=True"))
        if extra_fields.get("is_superuser")is not True :
            raise ValueError(_("Superusers must have a staff=True"))
       
       
       
       
	
     
    