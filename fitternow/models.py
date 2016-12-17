from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import user_logged_in
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

#built in django

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class UserProfile(models.Model):
    #user_profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateField(default='1900-01-22')
    gender = models.CharField(max_length=1, choices=(('F','FEMALE'),('M','MALE')), default='F')
    height = models.FloatField(default=170)
    weight = models.FloatField(default=60)
    user_notes = models.TextField(blank=True,null=True)
    secure_quest = models.CharField(max_length=200)
    secure_answer = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.user,self.gender,self.height,self.weight,self.user_notes,self.secure_quest,self.secure_answer)

class UserConsumption(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE, primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    nbdno = models.CharField(max_length=200)
    food_name = models.CharField(max_length=200)
    food_calories = models.FloatField(default=90)





class Activity(models.Model):
    act_id = models.AutoField(primary_key=True)
    activity_name = models.CharField(max_length=200)
    calories = models.FloatField(default=200)

    def __str__(self):
        return ' %s %s ' % (self.activity_name, self.calories)

class UserActivities(models.Model):
    user_act_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    duration = models.FloatField(default=1)
    calories_burned = models.FloatField(default=100)

    def __str__(self):
        return ' %s %s %s %s %s' % (self.user_act_id, self.user,self.activity_name,self.date_created,self.duration)




