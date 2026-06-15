from django.conf import settings
from django.db import models


class Intro(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='intros'
    )
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    hobby = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_at']