from rest_framework import viewsets
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer # noqa: E501

class MeasureUnitViewSet(viewsets.GenericViewSet):    
    serializer_class = MeasureUnitSerializer
    

class IndicatorViewSet(viewsets.GenericViewSet):    
    serializer_class = IndicatorSerializer
    

class CategoryProductViewSet(viewsets.GenericViewSet):    
    serializer_class = CategoryProductSerializer
    
    
    