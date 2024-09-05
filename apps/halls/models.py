from django.db import models

class Hall(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    rows = models.IntegerField(null=True, blank=True)
    seats_in_row = models.IntegerField(null=True, blank=True)

    @property
    def capacity(self):
        rows = self.rows if self.rows is not None else 0
        seats_in_row = self.seats_in_row if self.seats_in_row is not None else 0
        return rows * seats_in_row
