from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.views.decorators.csrf import csrf_exempt
from django.dispatch import receiver
from django.urls import reverse


# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    web = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    @csrf_exempt
    def createUser(sender, instance, created, **kwargs):
        if created:
            Account.objects.create(user=instance)

        # success_url = reverse_lazy('welcome')
    @receiver(post_save, sender=User)
    # @csrf_exempt
    def saveUser(sender, instance, **kwargs):
        # success_url = reverse_lazy('welcome')

        pass
        # instance.perfil.save()
    def get_absulute_url(self):
        return reverse('welcome')