from django.db import models

# Create your models here.
class Bio(models.Model):
    name = models.CharField(max_length=100)
    introduction = models.TextField()
    career_goal = models.TextField()

class Experience(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # This allows you to order your experiences
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title