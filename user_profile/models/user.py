from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Role(models.TextChoices):
        ADMIN = "admin", _("Admin")
        PROJECT_MANAGER = "project_manager", _("Project Manager")
        DEVELOPER = "developer", _("Developer")
        RESPONSER = "responser", _("Responser")
        STAKEHOLDER = "STAKEHOLDER", _("Stakeholder")
        CLIENT = "CLIENT", _("Client")

    role = models.CharField(
        _("função"),
        max_length=20,
        choices=Role.choices,
        default=Role.DEVELOPER,
        help_text="A função do usuário no sistema",
    )

    phone_number = models.CharField(
        _("telefone"),
        max_length=20,
        blank=True,
        null=True,
        help_text=_("Número de telefone para contato."),
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
