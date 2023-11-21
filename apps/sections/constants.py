# iterable 
from django.db import models
from django.utils.translation import gettext_lazy as _


class LevelChoices(models.IntegerChoices):
    BEGGINER = 0, _('Less than a year')
    MEDIUM = 1, _('Between 1 a 3 years')
    ADVANCE = 2, _('More than 3 years')


class SkillChoices(models.IntegerChoices):
    APTITUDES = 0, _('Aptitudes')
    CERTIFICATIONS = 1, _('Certifications')
    OTHER_SKILLS = 2, _('Other Skillls')
    SOFT_SKILLS = 3, _('Soft Skills')
    LANGUAGE = 4, _('Languages')


class InteractFieldsChoices(models.TextChoices):
    LIKE = "1", "LIKE"
    SHARE = "2", "SHARE"
    VIEW = "3", "VIEW"


class ContactTypeChoices(models.IntegerChoices):
    MOBILE = 0, _('Mobile')
    EMAIL = 1, _('Email')


class CategorySkillChoices(models.IntegerChoices):
    PROGRAMING_LANG = 0, _('Programing Languages')
    WEB_DEVELOPMENT = 1, _('Web Development')
    AUTOMATION = 2, _('Automation')
    DATA_ANALYTICS_VIZ = 3, _('Data Analytics & Visualization')
    DATABASES = 4, _('Databases')
    MANAGAMENT_TOOLS = 5, _('Management tools')
    DESIGN_TOOLS = 6, _('Design tools')
    CLOUD = 7, _('Cloud')
    OTHER = 8, _('Other')
    DATA_ENGINEER = 9, _('Data Engineering')


class EducationChoices(models.IntegerChoices):
    UNIVERSITY = 0, _('University')
    HIGH_SCHOOL = 1, _('High Scholl')


class EducationStatusChoices(models.IntegerChoices):
    COMPLETED = 0, _('Completed')
    INCOMPLETED = 1, _('Incompleted')
