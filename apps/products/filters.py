# from .models import Product, Category
#
# import django_filters
#
#
# class ProductFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(lookup_expr='icontains')
#     price = django_filters.NumberFilter()
#     price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label="цена от")
#     price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label="цена до")
#
#     category = django_filters.ModelChoiceFilter(
#         field_name="category",
#         queryset=Category.objects.all(),
#         empty_label='Все категории'
#     )
#
#     class Meta:
#         models = Product
#         fields = ["price", "title", "category"]