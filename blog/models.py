from django.db import models


class Post(models.Model):
	"""
	Blog post constructor.
	> id primary key
	> title of blog entry
	> body of blog entry
	> date of blog entry
	"""
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=140)
	body = models.TextField()
	signature = models.CharField(max_length=140, default="pavlovs_khat")
	date = models.DateTimeField()

def __str__(self):
	"""
	Blog post to string method.
	"""
	return self.title
