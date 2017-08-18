from django.db import models


class DumbTable(models.Model):
    name_field = models.CharField(max_length=15)
    number_field1 = models.IntegerField()
    number_field2 = models.IntegerField()
    number_field3 = models.IntegerField()

    def __str__(self):
        return self.name_field