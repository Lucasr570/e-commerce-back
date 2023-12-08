from django.urls import path
from apps.products.api.view.general_views import MeasureUnitViewSet, IndicatorViewSet  # noqa: E501
urlpatterns = [
    path('measure_unit/',MeasureUnitViewSet,name= 'measure_unit'),
    path('indicator/',IndicatorViewSet,name= 'indicator'),
]