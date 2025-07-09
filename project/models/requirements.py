from django.db import models
from django.utils.translation import gettext_lazy as _

from project.models.project import Project


class Requirements(models.Model):
    name = models.CharField(_("Nome do requisito"), max_length=255)
    description = models.TextField(_("Descrição do requisito"), blank=True, null=True)

    class RequirementType(models.TextChoices):
        FUNCTIONAL = "funcional", _("Funcional")
        NON_FUNCTIONAL = "nao_funcional", _("Não Funcional")

    requirement_type = models.CharField(
        _("Tipo de requisito"),
        max_length=20,
        choices=RequirementType.choices,
        default=RequirementType.FUNCTIONAL,
    )

    project = models.ForeignKey(
        Project, verbose_name=_("Projeto"), on_delete=models.PROTECT, related_name="fk_requirement_project"
    )

    created_at = models.DateTimeField(auto_now_add=True)
