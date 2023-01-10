from django.urls import path

from Elite_eats_app.views import DirectoryView, PostView, HomePageView, SearchResultsView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('directory.html', DirectoryView.as_view(), name='directory'),
    path('review.html', PostView.as_view(), name='review'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    ]

