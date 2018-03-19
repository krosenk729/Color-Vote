from django.db import models
# from colorful.fields import RGBColorField

class Word(models.Model):
	name = models.CharField(max_length=20)
	
	def __str__(self):
		return self.name

class Vote(models.Model):
	color = models.CharField(max_length=7)
	word = models.ForeignKey(Word, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.color + " " + self.word.name
	
	def red(self):
		return self.color[1:3]
	
	def green(self):
		return self.color[3:5]
	
	def blue(self):
		return self.color[5:7]
