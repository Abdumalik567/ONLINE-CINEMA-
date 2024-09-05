from rest_framework.routers import DefaultRouter


from apps.comments import views


router = DefaultRouter()
router.register('comment',views.CommentViewSet,basename='comment')


urlpatterns = [
]

urlpatterns += router.urls