from django.db import models

class User(models.Model):
    use_in_migrations = True
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    rank = models.IntegerField(default=1)
    point = models.IntegerField(default=0)

    class Meta:
        db_table = "users"
