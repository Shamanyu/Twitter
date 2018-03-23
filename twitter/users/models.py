from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)

# class Following(models.Model):
#     following_user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
#     follower_user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

class Tweets(models.Model):
    tweet_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
