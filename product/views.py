from django.shortcuts import render, get_object_or_404
from .models import Brand
from taggit.models import Tag
from .filters import ProductFilter
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)


def home(request):
    context = {
        'posts': Brand.objects.all()
    }
    return render(request, 'product/home.html', context)


class BrandListView(ListView):
    model = Brand
    template_name = 'product/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'brands'
    ordering = ['-created']

    # paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context


class BrandCreateView(CreateView):
    model = Brand
    fields = ['title', 'website', 'tags']

    def form_valid(self, form):
        return super().form_valid(form)


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'product/brand_detail.html'


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name
    brands = Brand.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'brands': brands,
    }
    return render(request, 'product/home.html', context)
