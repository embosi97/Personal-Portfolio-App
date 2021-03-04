from django.db import models

# Create your models here.
class Blog(models.Model):
    #consulted django documentation for Model fields
    title = models.CharField(max_length = 90)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
