from django.db import models

class SUser(models.Model):
    use_in_migrations = True
    s_user_id = models.AutoField(primary_key=True)
    email = models.TextField()
    nickname = models.TextField()
    password = models.TextField()
    point = models.TextField()

    class Meta:
        db_table = "s_users"

    def __str__(self):
        return f'{self.pk} {self.email} {self.nickname} {self.password} {self.point}'
