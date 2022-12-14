from django.db import models



class Delivery(models.Model):
    use_in_migration = True
    delivery_id = models.AutoField(primary_key=True)
    username = models.TextField()
    address = models.TextField()
    detail_address = models.TextField()
    phone = models.TextField()


    class Meta:
        db_table = "s_deliveries"

    def __str__(self):
        return f'{self.pk} {self.username} {self.address} {self.detail_address} {self.phone}'
