from django.db import models

from movie.m_users.models import MUser
from movie.showtimes.models import Showtime
from movie.theaters.models import Theater


class TheaterTicket(models.Model):
    use_in_migration = True
    theater_ticket_id = models.AutoField(primary_key=True)
    x = models.IntegerField()
    y = models.IntegerField()

    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    m_user = models.ForeignKey(MUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "m_theater_tickets"

    def __str__(self):
        return f'{self.pk} {self.x} {self.y}'
