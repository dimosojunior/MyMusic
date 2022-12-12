
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('base/', views.base, name="base"),
    path('trending/', views.trending, name="trending"),
    path('featured/', views.featured, name="featured"),
    path('new_release/', views.new_release, name="new_release"),


    path('view_music/<int:id>/', views.view_music, name="view_music"),
    path('bongo_flavor/', views.bongo_flavor, name="bongo_flavor"),
    path('hiphop/', views.hiphop, name="hiphop"),
    path('rnb/', views.rnb, name="rnb"),



    path('search_music/', views.search_music, name="search_music"),
    path('search_music_autocomplete/', views.search_music_autocomplete, name="search_music_autocomplete"),


    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),


    path('upload_music/', views.upload_music, name="upload_music"),








    #-------------------------------TUTORIALS------------------------------

    path('tutorials_home/', views.tutorials_home, name="tutorials_home"),
    path('view_tutorial/<int:id>/', views.view_tutorial, name="view_tutorial"),

    path('python/', views.python, name="python"),
    path('django/', views.django, name="django"),
    path('javascript/', views.javascript, name="javascript"),
    path('html_css/', views.html_css, name="html_css"),
    path('bootstrap/', views.bootstrap, name="bootstrap"),




    path('send_email/', views.send_email, name="send_email"),
    path('search_tutorial/', views.search_tutorial, name="search_tutorial"),
    path('search_tutorial_autocomplete/', views.search_tutorial_autocomplete, name="search_tutorial_autocomplete"),
    

]

