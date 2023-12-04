from django.db import models

# Create your models here. After creating the models, you should add them to the app's admin.py


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return f"{self.title}"
