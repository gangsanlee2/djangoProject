from django.db import models

class MUser(models.Model):
    use_in_migration = True
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=120, unique=True)
    nickname = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)
    age = models.IntegerField()

    class Meta:
        db_table = "m_users"
