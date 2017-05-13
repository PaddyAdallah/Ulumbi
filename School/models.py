from django.db import models


class Home(models.Model):
    writings = models.TextField()

    def __str__(self):
        return self.writings
