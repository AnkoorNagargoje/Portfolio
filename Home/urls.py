from django.urls import path
from .views import home_view, blog_home


urlpatterns = [
    path('', home_view),
    path('blog/', blog_home),
]