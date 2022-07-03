from django.urls import path, include
from snippets import views
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'snippet', SnippetViewSet)


urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('', include(router.urls)),
]