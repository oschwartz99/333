import datetime
from haystack import indexes
from .models import CustomUser


class UserIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	username = indexes.CharField(model_attr='username')
	email = indexes.CharField(model_attr='email')
	first_name = indexes.CharField(model_attr="first_name")
	last_name = indexes.CharField(model_attr="last_name")

	def get_model(self):
		return CustomUser

