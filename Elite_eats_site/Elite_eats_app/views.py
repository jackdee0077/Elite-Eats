from django.shortcuts import render

from django.db.models import Q
from django.views.generic import TemplateView, ListView


from. models import Restaurant

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Restaurant
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Restaurant.objects.filter(
            Q(name__icontains=query) | Q(address__icontains=query) | Q(city__icontains=query) | Q(state__icontains=query) | Q(zip_code__icontains=query)
        )
        return object_list
        #return Restaurant.objects.filter(name__icontains='Licky')
    

from django.views import View
from Elite_eats_app.models import Restaurant, Post
from Elite_eats_app.forms import PostForm

# Create your views here.

class DirectoryView(View):
    def get(self, request):
        restaurants = Restaurant.objects.all()

        html_data = {
            'restaurant_list': restaurants
        }

        return render(
            request=request,
            template_name='directory.html',
            context=html_data,
            )

class PostView(View):
    def get(self, request):
        review_form = PostForm()
        reviews = Post.objects.all()

        html_data = {
            'all_reviews': reviews,
            'form': review_form,
        }

        return render(
            request=request,
            template_name='review.html',
            context=html_data,
        )

    def post(self, request):
        reviews = Post.objects.all()

        print(request.POST)
        review_form = PostForm(request.POST)
        review_form.save()

        html_data = {
            'all_reviews': reviews,
            'form': review_form
        }

        return render(
            request=request,
            template_name='review.html',
            context=html_data,
        )