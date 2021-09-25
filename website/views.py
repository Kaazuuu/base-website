from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"
    
class Page1_1(TemplateView):
    template_name = "page1_1.html"