from django.db import models

class BUser(models.Model):
    use_in_migrations = True
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=120, unique=True)
    nickname = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = "b_users"