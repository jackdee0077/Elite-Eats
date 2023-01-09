from django.urls import path


from. views import HomePageView, SearchResultsView

urlpatterns = [
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("", HomePageView.as_view(), name="home"),
]

from Elite_eats_app.views import DirectoryView, PostView


urlpatterns = [
    path('directory.html', DirectoryView.as_view(), name='directory'),
    path('review.html', PostView.as_view(), name='review'),
    ]

