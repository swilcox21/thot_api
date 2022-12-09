from django.db import models

# Create your models here.
class Reminder(models.Model):
    owner = models.ForeignKey('auth.User', related_name='reminders', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=5000)
    due_date = models.DateTimeField(auto_now_add=True)
    recurring = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return self.text