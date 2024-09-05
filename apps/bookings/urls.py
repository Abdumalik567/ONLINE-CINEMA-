from rest_framework.routers import DefaultRouter


from apps.bookings import views


router = DefaultRouter()
router.register('booking',views.BookingViewSet,basename='booking')


urlpatterns = [
]

urlpatterns += router.urls