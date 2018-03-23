from django.test import TestCase
from .models import Word, Vote

class WordModelTests(TestCase):
	def word_is_a_string(self):
		w = Word(name="prayerful")
		self.assertIs(type(w),str)

class VoteModelTests(TestCase):
	def red_is_two_length(self):
		v = Vote(color="#ababab")
		self.assertIs(len(v.red()),2)
	def red_is_valid_hex_range(self):
		v = Vote(color="#ababab")
		r = int(v.red(), 16) <= 255
		self.assertIs(len(v.red()),True)
