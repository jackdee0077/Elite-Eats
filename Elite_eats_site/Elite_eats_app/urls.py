from django.urls import path
from Elite_eats_app.views import DirectoryView, PostView


urlpatterns = [
    path('directory.html', DirectoryView.as_view(), name='directory'),
    path('review.html', PostView.as_view(), name='review'),
    ]