from django.db import models

# Create your models here.
class TimespamtedModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Post(TimespamtedModel):
    title=models.CharField(max_length=255)
    body=models.TextField(max_length=255)
    

    def __str__(self):
        return self.title
