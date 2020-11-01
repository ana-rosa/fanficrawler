from django.views.generic import DetailView, ListView, TemplateView
from .models import Fandom, Language


class HomeView(TemplateView):
    template_name = "home.html"
    

class FandomListView(ListView):
    template_name = "fandoms.html"
    model = Fandom
    context_object_name = "fandoms" 
    queryset = Fandom.objects.all()
    

class LanguageListView(ListView):
    template_name = "languages.html"
    model = Language
    context_object_name = "languages"
    queryset = Language.objects.order_by('name')


class FandomDetailView(DetailView):
    template_name = "fandom-detail.html"
    model = Fandom
    context_object_name = "fandom" 
    
    
class LanguageDetailView(DetailView):
    template_name = "language-detail.html"
    model = Language
    context_object_name = "language"
     
    
