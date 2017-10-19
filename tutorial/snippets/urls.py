from django.conf.urls import url, include
#from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.schemas import get_schema_view




# urlpatterns = format_suffix_patterns([
#    # url(r'^snippets/$', views.snippet_list),
#    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
#     url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
#     url(r'^users/$', views.UserList.as_view(), name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
#     url(r'^$', views.api_root),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
# ])

# Create a router and register our viewsets with it.
router=DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

### ViewSet url



schema_view = get_schema_view(title='Pastebin API')
# Login and logout views for the browsable API
urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]