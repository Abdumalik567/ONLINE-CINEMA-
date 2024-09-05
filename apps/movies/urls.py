from rest_framework.routers import DefaultRouter
from django.urls import path,include


from apps.movies import views


router = DefaultRouter()
router.register('movies',views.MovieViewSet,basename='movie')
router.register('likes', views.LikeViewSet, basename='like')
router.register('payments', views.PaymentViewSet, basename='payment')
router.register('subtitles', views.SubtitleViewSet,basename='subtitle')
router.register('genres', views.GenreViewSet,basename='genre')
router.register('awards', views.AwardViewSet,basename='award')
router.register('wishlists', views.WishlistViewSet,basename='wishlist')
router.register('actors', views.ActorViewSet,basename='actor')
router.register('moviesessions', views.MovieSessionViewSet,basename='moviesession')
router.register('orders', views.OrderViewSet,basename='order')


urlpatterns = [
    path('', include(router.urls)),
]