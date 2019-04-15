from haystack import indexes
from .models import Event


class EventIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	created_by = indexes.CharField(model_attr='user')
	event_name = indexes.CharField(model_attr='event_name')
	event_type = indexes.CharField(model_attr='event_type')
	public = indexes.CharField(model_attr='public')
	location = indexes.CharField(model_attr='location')


	def get_model(self):
		return Event