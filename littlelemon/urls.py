from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurant.views import MenuViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
