from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),

    path('', include('core.urls')),  # all app URLs here
]

from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),

    path('', views.home, name='home'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
]