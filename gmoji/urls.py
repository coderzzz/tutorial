from django.conf.urls import url
from gmoji import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # url(r'^gmojis/$', views.gmoji_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.gmoji_detail),
    url(r'^gmojis/$', views.GmojiList.as_view()),
]



urlpatterns = format_suffix_patterns(urlpatterns)
