from django.db import models

class Project(models.Model):
    #consulted django documentation for Model fields
    title = models.CharField(max_length = 90)
    description = models.CharField(max_length = 300)
    image = models.ImageField(upload_to = 'portfolio/images/')
    url = models.URLField(blank = True) #blank == null

    def __str__(self):
        return self.title
