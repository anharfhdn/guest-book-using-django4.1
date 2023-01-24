from django.db import models

# Create your models here.
class Tamu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    message = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        db_table = 'guestbook_databases'