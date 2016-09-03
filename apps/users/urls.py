from django.conf.urls import url
from .views import Users, Filter

urlpatterns = [
    url(r'^$', Users.as_view(), name='users'),
    url(r'^filter$', Filter.as_view(), name='filter')
]
