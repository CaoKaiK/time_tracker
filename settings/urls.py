


from django.urls import include, path

from settings.views import ContractListView, manage_tags


urlpatterns = [
    path('', ContractListView.as_view(), name='settings-personal'),
    path('tags/', manage_tags, name='settings-tags')
]
