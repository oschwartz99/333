from haystack import indexes
from .models import CustomUser


class UserIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.EdgeNgramField(document=True, use_template=True)
	username = indexes.EdgeNgramField(model_attr="username")
	first_name = indexes.CharField(model_attr="first_name")
	last_name = indexes.CharField(model_attr="last_name")

	def get_model(self):
		return CustomUser
