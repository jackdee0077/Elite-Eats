from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.views import View
from .models import Restaurant
from Elite_eats_app.models import Restaurant, Post, Image
from Elite_eats_app.forms import PostForm, ImageForm
#from .forms import ImageForm
from django.http import HttpResponseRedirect
# from django.views.generic import 
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = 'home.html'
    

class TrendingView(View):
    def get(self, request):
        restaurants = Restaurant.objects.all()

        html_data = {
            'restaurant_list': restaurants
        }

        return render(
            request=request,
            template_name='trending.html',
            context=html_data,
            )

class SearchResultsView(ListView):
    model = Restaurant
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Restaurant.objects.filter(
            Q(name__icontains=query) | Q(address__icontains=query) | Q(city__icontains=query) | Q(state__icontains=query) | Q(zip_code__icontains=query)
        )
        return object_list
        # return Restaurant.objects.filter(name__icontains='Licky')
    
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
    
    submitted = False

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
class ImageUploadView(View):
    submitted = False
    model = Image
    form_class = ImageForm
    success_url = reverse_lazy('home')
    template_name = 'upload.html'

    def get(self, request,*args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': ImageForm})

        html_data = {
                'image': form,
                'from': form }

        return render(
            request=request,
            template_name='home.html',
            context=html_data,
        )
        
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():

            print(request.POST)
            form = ImageForm(request.POST)
            form.save()

            html_data = {
                'image': form,
                'from': form }

        return render(
            request=request,
            template_name='home.html',
            context=html_data,
        )

       
