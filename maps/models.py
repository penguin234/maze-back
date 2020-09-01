from django.db import models

# Create your models here.


class Stage(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Blueprint(models.Model):
    description = models.TextField()
    verticals = models.TextField()
    horizontals = models.TextField()

    def __str__(self):
        return self.description[:200]

class Level(models.Model):
    levelno = models.IntegerField()
    title = models.CharField(max_length=200)
    blueprint = models.OneToOneField(Blueprint, on_delete=models.CASCADE)

    stage = models.ForeignKey(Stage, related_name='levels', on_delete=models.CASCADE)