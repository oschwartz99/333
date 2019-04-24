from haystack import indexes
from .models import Event


class EventIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.EdgeNgramField(document=True, use_template=True)
	event_name = indexes.CharField(model_attr='event_name')
	event_descr = indexes.CharField(model_attr='event_descr')
	location = indexes.CharField(model_attr='location')
	created_by = indexes.CharField(model_attr='user')
	event_type = indexes.CharField(model_attr='event_type')
	public = indexes.BooleanField(model_attr='public')
	lng = indexes.FloatField(model_attr='lng')
	lat = indexes.FloatField(model_attr='lat')
	id = indexes.CharField(model_attr='pk')

	def get_model(self):
		return Event