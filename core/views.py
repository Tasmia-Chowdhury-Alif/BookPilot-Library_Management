from django.shortcuts import render
from django.views.generic import ListView
from books.models import Book
from category.models import Category
from django.http import Http404

# Create your views here.
class HomeView(ListView):
    model = Book 
    template_name = 'home.html'
    context_object_name = 'books'

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        
        if category_slug:
            try:
                category = Category.objects.get(slug=category_slug)

            except Category.DoesNotExist: # handleing where the brand doesn't exixts but someone requested get request  
                raise Http404("Category not found")
            
            return Book.objects.filter(category= category)
        
        return Book.objects.all()
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
    
    