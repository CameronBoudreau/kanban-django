from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/tasks/$', views.card_list),
    url(r'^api/tasks/(?P<pk>[0-9]+)/$', views.card_detail)
]
