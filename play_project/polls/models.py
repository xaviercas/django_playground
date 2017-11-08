from django.db import models

class Question(models.Model):
	ques_text = models.CharField(max_length=200)
	ques_pubdate = models.DateTimeField('date published')
	def __str__(self):
		return self.ques_text

class Choice(models.Model):
	ques_id = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	choice_votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text
