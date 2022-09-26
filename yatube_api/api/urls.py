from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, GroupViewSet, FollowViewSet, CommentViewSet


router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='subscriptions')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments'
                )


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
