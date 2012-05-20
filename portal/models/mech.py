class Mech(models.Model):
    name = models.CharField(max_length=50)
    tonnage = models.IntegerField()