from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class Portfolio(AbstractUser):
    MALE = 'm'
    FEMALE = 'f'
    DEFAULT_GENDER_CHOICES = (
        (MALE, _('Male')),
        (FEMALE, _('Female')),
    )
    date_of_birth = models.DateField(_("Date of birth"), blank=True, null=True)
    gender = models.CharField(_("Gender"), max_length=1, choices=DEFAULT_GENDER_CHOICES,
                              default=MALE)
    phone_number = models.CharField(_("Phone Number"), max_length=15, null=True, blank=True)
    about_me = models.TextField(_("About Me"), null=True, blank=True)
    profile_image = models.ImageField(_("Profile Image"), null=True, blank=True)
    home_town = models.CharField(_('Home Town'), max_length=100, null=True, blank=True)
    address = models.CharField(_("Address"), max_length=255, null=True, blank=True)
    city = models.CharField(_("City"), max_length=100, null=True, blank=True)
    pin = models.CharField(_("Pin"), max_length=10, null=True, blank=True)
    country = models.CharField(_("Country"), max_length=100, null=True, blank=True)
    website = models.CharField(_("Website"), max_length=100, null=True, blank=True)

    # Summery
    career_objective = models.TextField(_("Career Objective"), null=True, blank=True)
    employment_profile = models.TextField(_("Employment Profile"), null=True, blank=True)
    academic_record = models.TextField(_("Academic Records"), null=True, blank=True)
    personal_skills = models.TextField(_("Personal Skills"), null=True, blank=True)

    # activity
    number_of_clients = models.IntegerField(null=True, blank=True)
    number_of_projects = models.IntegerField(null=True, blank=True)
    number_of_lines_of_code = models.IntegerField(null=True, blank=True)

    # Social media links
    facebook = models.URLField(_("Facebook"), max_length=100, null=True, blank=True)
    twitter = models.URLField(_("Twitter"), max_length=100, null=True, blank=True)
    linked_in = models.URLField(_("LinkedIn"), max_length=100, null=True, blank=True)
    stack_overflow = models.URLField(_("StackOverflow"), max_length=100, null=True, blank=True)
    github = models.URLField(_("Github"), max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.username


class Projects(models.Model):
    user = models.ForeignKey(Portfolio, related_name="get_projects")
    name = models.CharField(max_length=100, )
    image = models.ImageField(upload_to="uploads/")
    thumbnail = models.ImageField(upload_to="uploads/thumb/")
    description = models.TextField()

    def __unicode__(self):
        return self.name


class TechnicalExpertise(models.Model):
    user = models.ForeignKey(Portfolio, related_name="get_technical_expertise")
    title = models.CharField(max_length=100)
    items = models.ManyToManyField('home.Items')

    def __unicode__(self):
        return self.title


class Items(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Quotes(models.Model):
    user = models.ForeignKey(Portfolio, related_name="get_quotes")
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    text = models.TextField()

    def __unicode__(self):
        return self.name
