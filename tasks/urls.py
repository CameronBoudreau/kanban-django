from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic.base import RedirectView
from . import views


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/main/', permanent=False),
        name='redirect'),
    url(r'^main/$', views.MainPage.as_view()),
    url(r'^api/tasks/$', views.CardList.as_view()),
    url(r'^api/tasks/(?P<pk>[0-9]+)/$', views.CardDetail.as_view()),
    url(r'^api/users/$', views.UserList.as_view()),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
