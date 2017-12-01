from django.conf.urls import url

from blog.views import PostList, PostDetail

urlpatterns = [
    url(
        r'^$',
        PostList.as_view(),
        name = 'main'
    ),
    url(
        r'^(?P<pk>\d+)/$',
        PostDetail.as_view(),
        name = 'posts',
    ),
]