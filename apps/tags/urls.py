from rest_framework.routers import DefaultRouter


from apps.tags import views


router = DefaultRouter()
router.register('tag',views.TagViewSet,basename='tag')


urlpatterns = [
]

urlpatterns += router.urls