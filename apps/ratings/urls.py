from rest_framework.routers import DefaultRouter


from apps.ratings import views


router = DefaultRouter()
router.register('rating',views.RatingViewSet,basename='rating')


urlpatterns = [
]

urlpatterns += router.urls