from django.db import models

# Create your models here.
class userProfile(models.Model):
    nickname = models.CharField(max_length = 120)
    about = models.TextField()

    def _str_(self):
        return self.nickname