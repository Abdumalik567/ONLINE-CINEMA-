from rest_framework.routers import DefaultRouter


from apps.halls import views


router = DefaultRouter()
router.register('hall',views.HallViewSet,basename='hall')


urlpatterns = [
]

urlpatterns += router.urls