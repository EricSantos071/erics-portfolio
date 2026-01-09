from django.db import models

# Create your models here.
class Bio(models.Model):
    name = models.CharField(max_length=100)
    introduction = models.TextField()
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    what_i_know = models.TextField(help_text="Separate items with new lines")
    how_i_learn = models.TextField()
    my_goals = models.TextField()

class Experience(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # This allows you to order your experiences
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title