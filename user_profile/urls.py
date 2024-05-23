from django.urls import path
from . import views
urlpatterns = [

        path('user/',views.user,name='user'),
        path('login/', views.login_user, name='login'),
        path('register/', views.register_user, name='register_user'),
        path('logout/', views.logout_user, name='logout'),
        path('profile/', views.profile, name='profile'),
        path('change_profile_picture/', views.change_profile_picture, name='change_profile_picture'),
        path('view_user_information/<str:username>/', views.view_user_information, name='view_user_information'),
        path('follow_or_unfollow/<int:user_id>/', views.follow_or_unfollow_user, name='follow_or_unfollow_user'),
        path('user_notifications/', views.user_notifications, name='user_notifications'),
        path('mute_or_unmute_user/<int:user_id>/', views.mute_or_unmute_user, name='mute_or_unmute_user'),

]