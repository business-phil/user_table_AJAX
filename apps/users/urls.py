from django.conf.urls import url
from .views import Users, Create

urlpatterns = [
    url(r'^$', Users.as_view(), name='index'),
    url(r'^create$', Create.as_view(), name='create')
]
