from django.db import models

class User(models.Model):
    id = models.CharField(max_length=9, primary_key=True)
    real_name = models.CharField(max_length=256, blank=False)
    tz = models.CharField(max_length=256,blank=False)

    def __str__(self):
        return self.real_name

class ActivityPeriod(models.Model):
    start_time = models.DateTimeField(blank=False)
    end_time = models.DateTimeField(blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='activity_periods')

