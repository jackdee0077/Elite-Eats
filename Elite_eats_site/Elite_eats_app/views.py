#from django.shortcuts import render
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
    

# Create your views here.
