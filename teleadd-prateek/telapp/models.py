from django.db import models

class ClientApiKey(models.Model):
    apikey = models.CharField(max_length=100)
    apihash = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=13)

    def __str__(self):
        return self.mobile_no
