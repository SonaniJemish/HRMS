from django.db import models
from django.utils.translation import gettext_lazy as _


class GenderTypeChoice(models.TextChoices):
    MALE = ("MALE", _("MALE"))
    FEMALE = ("FEMALE", _("FEMALE"))

