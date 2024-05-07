from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vendor.views import VendorViewSet
from purchase_order.views import PurchaseOrderViewSet
from vendor_performance.views import HistorialPerformanceViewSet

router = DefaultRouter()

# Registering the VendorViewSet and PurchaseOrderViewSet
router.register('vendor',VendorViewSet,basename='vendor')
router.register('purchase-order',PurchaseOrderViewSet,basename='purchase_order')

# Defining URL patterns
urlpatterns = [
    # Include the URLs generated by the router
    path('',include(router.urls)),

    # Endpoint for getting historical performance of vendors
    path('vendor/historical_performance',HistorialPerformanceViewSet.as_view({'get':'list'}),name='historical_performance'),
    
    # Endpoint for getting historical performance of a specific vendor
    path('vendor/historical_performance/<int:vendor_id>/',HistorialPerformanceViewSet.as_view({'get':'list'}),name='vendor_performance'),
]
