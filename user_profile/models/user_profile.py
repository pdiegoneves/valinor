from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, verbose_name=_("Profile"), on_delete=models.CASCADE
    )

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
        help_text="Telefone do usuário",
    )

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                UserProfile.objects.create(user=instance)
        except:
            pass

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass
