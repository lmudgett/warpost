class Clan(models.Model):
    name = models.CharField(max_length=50)
    formed = models.DateField()