from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    name = models.CharField(_("Nome do projeto"), max_length=255)
    description = models.TextField(_("Descrição do projeto"), blank=True, null=True)
    project_manager = models.ForeignKey(
        User,
        verbose_name=_("Gerente do projeto"),
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="fk_project_user_project_manager",
    )
    responser = models.ForeignKey(
        User,
        verbose_name=_("Responsável"),
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="fk_project_user_responser",
    )
    developer = models.ForeignKey(
        User,
        verbose_name=_("Desenvolvedor"),
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="fk_project_user_developer",
    )
    stackholder = models.ForeignKey(
        User,
        verbose_name=_("Stackholder"),
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="fk_project_user_stackholder",
    )
    client = models.ForeignKey(
        User, verbose_name=_("Cliente"), on_delete=models.PROTECT, blank=True, null=True,
        related_name="fk_project_user_project_client",
    )
    start_date = models.DateField(_("Data de início"), blank=True, null=True)
    estimated_end_date = models.DateField(
        _("Data prevista de término"), blank=True, null=True
    )
    end_date = models.DateField(_("Data de término"), blank=True, null=True)

    reasons = models.TextField(_("Motivos"), blank=True, null=True)
    quantitative_benefits = models.TextField(
        _("Benefícios quantitativos]"), blank=True, null=True
    )
    qualitative_benefits = models.TextField(
        _("Benefícios qualitativos"), blank=True, null=True
    )
    risks = models.TextField(_("Riscos"), blank=True, null=True)
    main_deliveries = models.TextField(_("Entregas principais"), blank=True, null=True)
    setup_cost = models.FloatField(_("Custo de configuração"), blank=True, null=True)
    recurring_cost = models.FloatField(_("Custo recorrente"), blank=True, null=True)

    # technologies = models.ManyToManyField(

    created_at = models.DateTimeField(auto_now_add=True)
