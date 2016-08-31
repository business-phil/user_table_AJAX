from django.conf.urls import url
from .views import Index, Create

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^create$', Create.as_view(), name='create')
]
