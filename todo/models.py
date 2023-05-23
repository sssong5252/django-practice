from django.db import models

# Create your models here.
class TodoList(models.Model):
	todo = models.CharField(max_length=30)
	description = models.TextField()
	important = models.BooleanField(default=False)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.todo} [{self.id}]'