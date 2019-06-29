from django.db import models

class Mapping1(models.Model):
    src = models.CharField(max_length=255, null=False)
    dest = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.src, self.dest)

