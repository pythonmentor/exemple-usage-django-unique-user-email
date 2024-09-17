from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name="utilisateur",
        on_delete=models.CASCADE,
    )
    full_name = models.CharField(
        "nom de l'utilisateur", max_length=255, blank=True
    )

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profils"

    def __str__(self) -> str:
        return self.user.email
