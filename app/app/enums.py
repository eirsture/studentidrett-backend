from enum import Enum

from django.db import models

from django.utils.translation import gettext_lazy as _


class Gender(models.TextChoices):
    MALE = "M", _("Male")
    FEMALE = "F", _("Female")
    MIX = "MX", _("Mix")
    ANY = "A", _("Any")


class Skill(models.TextChoices):
    NONE = "NONE", _("No expectations")
    LOW = "LOW", _("Low")
    MEDIUM = "MED", _("Medium")
    HIGH = "HI", _("High")
    PRO = "PRO", _("Professional")


class Status(models.TextChoices):
    OPEN = "OP", _("Open")
    CLOSED = "CL", _("Closed")
    FULL = "FU", _("Full")
    TRYOUTS = "TO", _("Tryouts")


class Region(models.TextChoices):
    NORD = "nord", _("Nord-Norge")
    MIDT = "midt", _("Midt-Norge")
    VEST = "vest", _("Vestlandet")
    SOR = "sor", _("Sørlandet")
    OST = "ost", _("Østlandet")


class EnvironmentOptions(Enum):
    BASE = "BASE"
    LOCAL = "LOCAL"
    DEVELOPMENT = "DEVELOPMENT"
    PRODUCTION = "PRODUCTION"
