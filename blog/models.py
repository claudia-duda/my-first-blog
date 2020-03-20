from django.conf import settings
from django.db import models
from django.utils import timezone

#models.Model = django model , them it's gonna save on date base
class Post(models.Model): #model object
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#link to other model
    title = models.CharField(max_length=200)#limit char type
    text = models.TextField()#free limit char type 
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)#time and hour type

    def publish(self):#methoud publish
        self.published_date = timezone.now()
        self.save()

    def __str__(self):#methoud return title
        return self.title