from rest_framework.routers import DefaultRouter


from apps.reviews import views


router = DefaultRouter()
router.register('review',views.ReviewViewSet,basename='review')


urlpatterns = [
]

urlpatterns += router.urls
