
from django.urls import path
from jumpmetric import views

urlpatterns = [
    ######## BACKEND URLS ########
    path("dashboard", views.dashboard, name="dashboard"),
    path("prepare_new_trial", views.prepare_new_trial, name="prepare_new_trial"),
    path("insert_new_trial", views.insert_new_trial, name="insert_new_trial"),
    # path("thanks", views.thanks, name="thanks"),

    path("display_all_trials", views.display_all_trials, name="display_all_trials"),
    path("display_selected_trial/<int:pk>", views.display_selected_trial, name="display_selected_trial"),
    path("calculate_trial", views.calculate_trial, name="calculate_trial"),

    ######## FRONTEND URLS ########
    path("", views.homepage, name="homepage"),
    path("about", views.about, name="about"),



    ######## USER URLS #########
    #User Reigster,Login,Sighup
    path('login', views.user_login, name='login'),
    path('signup', views.user_signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
    path('userslist', views.usersList, name='userslist')





    # #User Reigster,Login,Sighup
    # path('login', views.user_login, name='login'),
    # path('signup', views.user_signup, name='signup'),
    # path('logout', views.user_logout, name='logout'),
    # path('userslist', views.usersList, name='userslist')
]


