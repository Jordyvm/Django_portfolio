from django.db import models

# Create your models here.

class Skill(models.Model):
    skill = models.CharField(max_length=30)
    
    def __str__(self):
        return self.skill

    class Meta:
        ordering = ('skill',)

class Post(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(default='')

    skills = models.ManyToManyField(Skill)

    MediaTechnology = models.BooleanField(default=False)

    def __str__(self):
        return self.title
