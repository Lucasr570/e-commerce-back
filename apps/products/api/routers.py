from rest_framework.routers import DefaultRouter
from apps.products.api.view.general_views import ( MeasureUnitViewSet,IndicatorViewSet, 
    CategoryProductViewSet 
)                                                  
from apps.products.api.view.product_viewsets import ProductViewSet

router = DefaultRouter()
router.register(r'products',ProductViewSet,basename= 'products')
router.register(r'measure-unit',MeasureUnitViewSet,basename= 'measure_unit')
router.register(r'indicators',IndicatorViewSet,basename= 'indicators')
router.register(r'category-products',CategoryProductViewSet,basename= 'category_products') # noqa: E501

urlpatterns = router.urls