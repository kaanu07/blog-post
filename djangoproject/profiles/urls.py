from .views import ProfileDetailView
from django.conf.urls import url,include

urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(),name='detail'),
]
