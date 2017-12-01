from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    """ Модель поста """
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    title = models.CharField(max_length=25)
    changeTime = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=100)
    
    def get_article(self):
        return Post.objects.all()
    
    def __str__(self):
        return self.title


#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
    #if created:
        #Post.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
    #instance.profile.save()
    
    