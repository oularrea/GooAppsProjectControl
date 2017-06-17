from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _


class TypeProject(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(_("Name"), max_length=255, null=False, blank=False)

    class Meta:
        db_table="typeProject"
        verbose_name = _("Project Type")
        verbose_name_plural = _("Projects Type")


class StatusProject(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(_("Name"), max_length=255, null=False, blank=False)

    class Meta:
        db_table= "statusProject"
        verbose_name = _("Project Status")
        verbose_name_plural = _("Projects Status")


class Project(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(_("Name"), max_length=255, null=False, blank=False)
    typeProject = models.ForeignKey(TypeProject, related_name="types")
    statusProject = models.ForeignKey(StatusProject, related_name="status")

    class Meta:
        db_table = "project"
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
