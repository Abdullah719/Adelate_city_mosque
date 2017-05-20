from django.db import models
# Create your models here.
class Posts(models.Model):
    titles = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()


    def __str__(self):
        return self.titles

    def date_setting(self):
        return self.pub_date.strftime('%b %d %y')