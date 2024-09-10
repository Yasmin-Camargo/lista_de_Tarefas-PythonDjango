from datetime import date

from django.db import models


class Todo(models.Model):
    title = models.CharField(
        verbose_name="Título", max_length=100, null=False, blank=False
    )  # transforma em um varchar no banco de dados
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False
    )  # cria a data automaticamente
    deadline = models.DateField(verbose_name="Data de entrega", null=False, blank=True)
    finished_at = models.DateField(null=True)

    class Meta:
        ordering = ["deadline"]

    def mark_has_completed(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()