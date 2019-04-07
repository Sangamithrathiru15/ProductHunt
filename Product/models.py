from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
    title=models.CharField(max_length=50)
    url=models.URLField(max_length=200)
    pub_date=models.DateTimeField()
    votes_total=models.IntegerField(default=1)   
    image=models.ImageField(upload_to='prodimage/')
    icon=models.ImageField(upload_to='prodimage/')
    body=models.TextField(max_length=500)

    hunter=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        #to display the description in the admin page
        return self.title

    def summary(self):
        #to just display the part of blog description
        return self.body[:100]


    def pub_date_format(self):
        return self.pub_date.strftime('%b %e %Y')
