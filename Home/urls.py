from django.urls import path
from .views import home_view, blog_home, my_coding_journey


urlpatterns = [
    path('', home_view),
    path('blog/', blog_home),
    path('blog/my-coding-journey/', my_coding_journey)
]