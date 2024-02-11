from django.db import models

class MenuItems(models.Model):
    id = models.AutoField
    level = models.IntegerField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    menu_name = models.CharField(max_length=80)

    def __str__(self):
        return self.title