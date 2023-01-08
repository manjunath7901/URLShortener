from django.db import models

class LongToShort(models.Model):
    long_url=models.URLField(max_length=500)
    custom_name=models.CharField(max_length=500,unique=True)
    visit_count=models.IntegerField(default=0)
    created_date=models.DateField(auto_now=True)

# Create your models here.
