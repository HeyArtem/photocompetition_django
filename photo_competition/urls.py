from django.urls import path
from photo_competition.views.post.post import PostListView, PostCreateView
from photo_competition.views.user.user import UserRegisterView, UserLoginView, logout_user
from photo_competition.views.post.post import index

urlpatterns = [
    path('', PostListView.as_view(), name="index"),
    # path('', index, name="index"),
    path('post/create/', PostCreateView.as_view(), name="create"),

    path('user/login/', UserLoginView.as_view(), name="login"),
    path('user/register/', UserRegisterView.as_view(), name="register"),
    path('user/logout/', logout_user, name="logout"),

    # path('post/<slug:post_slug>/', ????, name='post')
]
