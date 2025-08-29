from django.db import models

class Club(models.Model):
    clubName = models.CharField(max_length=200)
    activeClub = models.booleanField(default=False)
    dateCreated = models.DateField()
    membersActive = 
    upcomingEvents = 


    def __str__(self):
        return f"{self.clubName}\n"

