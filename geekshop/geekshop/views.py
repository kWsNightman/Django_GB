from django.views.generic import ListView, TemplateView

from mainapp.models import Product


class IndexListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all()[:3]
    extra_context = {'title': 'магазин', 'products': queryset}


class ContactsTemplateView(TemplateView):
    template_name = 'contact.html'
    extra_context = {'title': 'контакты'}
