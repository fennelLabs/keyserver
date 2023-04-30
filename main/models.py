from django.db import models


class UserKeys(models.Model):
    user = models.CharField(max_length=256)
    mnemonic = models.CharField(max_length=256)

    def __str__(self):
        return self.user
