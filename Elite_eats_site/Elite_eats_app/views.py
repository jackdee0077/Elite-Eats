from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.views import View
from .models import Restaurant
from Elite_eats_app.models import Restaurant, Post
from Elite_eats_app.forms import PostForm

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
def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'home.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'home.html', {'form': form})