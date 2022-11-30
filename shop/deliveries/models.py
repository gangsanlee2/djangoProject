from django.db import models

from shop.s_users.models import SUser


class Delivery(models.Model):
    use_in_migration = True
    delivery_id = models.AutoField(primary_key=True)
    username = models.TextField()
    address = models.TextField()
    detail_address = models.TextField()
    phone = models.TextField()

    s_user = models.ForeignKey(SUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "s_deliveries"

    def __str__(self):
        return f'{self.pk} {self.username} {self.address} {self.detail_address} {self.phone}'
