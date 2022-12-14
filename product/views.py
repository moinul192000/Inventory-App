from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from .forms import ItemForm, ItemSizesForm
from .models import Item, ItemSizes


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'product_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item_form"] = self.form_class()
        context["item_sizes_form"] = ItemSizesForm()
        return context

    def form_valid(self, form):
        item = form.save()
        item_sizes_form = ItemSizesForm(self.request.POST)
        item_sizes = item_sizes_form.save(commit=False)
        item_sizes.item = item
        print(item_sizes)
        item_sizes.save()
        return redirect(reverse_lazy("items:detail", kwargs={"pk": item.pk}))

    def form_invalid(self, form):
        item_sizes_form = ItemSizesForm(self.request.POST)
        return self.render_to_response(
            self.get_context_data(
                item_form=form, item_sizes_form=item_sizes_form
            )
        )
    # def post(self, request, *args, **kwargs):
    #     item_form = ItemForm(request.POST, request.FILES)
    #     item_sizes_form = ItemSizesForm(request.POST)

    #     if item_form.is_valid() and item_sizes_form.is_valid():
    #         item = item_form.save()
    #         item_sizes = item_sizes_form.save(commit=False)
    #         item_sizes.item = item
    #         item_sizes.save()
    #         return redirect(reverse_lazy("items:detail", kwargs={"pk": item.pk}))

    #     return self.render_to_response(
    #         self.get_context_data(
    #             item_form=item_form, item_sizes_form=item_sizes_form
    #         )
    #     )


class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the sizes and stocks of each item
        sizes_and_stocks = []
        for item in self.object_list:
            sizes = ItemSizes.objects.filter(item=item)
            sizes_and_stocks.append([(size.size, size.stock)
                                    for size in sizes])

        context['item_with_sizes'] = zip(self.object_list, sizes_and_stocks)
        print(context['item_with_sizes'])
        return context
