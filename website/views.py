from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"
    
class Article_1(TemplateView):
    template_name = "article_1.html"