from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib import messages
from .models import Content
from product.models import Brand
from django.views.generic import DetailView


class UserChartView(DetailView):
    template_name = 'product/brand_detail.html'

    def get_object(self):
        pk = self.kwargs.get('brand_slug')
        return pk

    def get_context_data(self, **kwargs):
        context = super(UserChartView, self).get_context_data(**kwargs)
        brand = Brand.objects.get(slug=self.get_object())
        qs = brand.content_set.all()
        context["qs"] = qs
        return context


def content_view(request, brand_slug):
    brand = Brand.objects.get(slug=brand_slug)
    ContentFormset = inlineformset_factory(Brand, Content, fields='__all__', extra=1)
    if request.method == 'POST':
        formset = ContentFormset(request.POST, instance=brand)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'chart is updated')
            return redirect('Brand-Detail', brand_slug=brand.slug)
    formset = ContentFormset(instance=brand)
    qs = brand.content_set.all()
    context = {
        'formset': formset,
        'qs': qs,
    }
    return render(request, 'chart/chartcontent.html', context)
