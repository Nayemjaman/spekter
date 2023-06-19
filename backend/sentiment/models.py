from django.db import models

# Create your models here.


class Analysis(models.Model):
    text = models.TextField()

    def __str__(self) -> str:
        return self.text
