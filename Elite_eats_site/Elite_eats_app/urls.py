from django.urls import path

from Elite_eats_app.views import DirectoryView, PostView, HomePageView, SearchResultsView, TrendingView, ImageUploadView, update_review, delete_review

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path('directory.html', DirectoryView.as_view(), name='directory'),
    path('review.html', PostView.as_view(), name='review'),
    path("search/", SearchResultsView.as_view(), name='search_results'),
    path('trending.html', TrendingView.as_view(), name='trending'),
    path('upload', ImageUploadView.as_view(), name='upload'),
    path('update_review/<int:review_id>', update_review, name='update-review'),
    path('delete_review/<int:review_id>', delete_review, name='delete-review'),
    ]

