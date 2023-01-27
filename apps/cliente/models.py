from django.db import models


class Cliente(models.Model):
    nombres = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.nombres + ' ' + self.email + ' ' + self.password

    class Meta:
        db_table = 'api_cliente'
