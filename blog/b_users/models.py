from django.db import models

class BUser(models.Model):
    use_in_migrations = True
    b_user_id = models.AutoField(primary_key=True)
    email = models.TextField()
    nickname = models.TextField()
    password = models.TextField()

    class Meta:
        db_table = "b_users"
        verbose_name = 'user'
        verbose_name_plural = 'b_users'

    def __str__(self):
        return f'{self.pk} {self.email} {self.nickname} {self.password}'