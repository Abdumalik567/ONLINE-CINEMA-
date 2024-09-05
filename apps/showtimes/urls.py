from rest_framework.routers import DefaultRouter


from apps.showtimes import views


router = DefaultRouter()
router.register('showtime',views.ShowtimeViewSet,basename='showtime')


urlpatterns = [
]

urlpatterns += router.urls
