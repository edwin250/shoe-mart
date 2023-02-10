from django.urls import path
from frontend import views

urlpatterns = [

    path('', views.home_pg, name="home_pg"),
    path('about_pg/', views.about_pg, name="about_pg"),
    path('contact_pg/', views.contact_pg, name="contact_pg"),
    path('contacts1/',views.contacts1,name="contacts1"),
    path('dispCateg/<itemCateg>', views.dispCateg, name="dispCateg"),
    path('displayProd/<int:dataid>/', views.displayProd, name="displayProd"),
    path('login/', views.login, name='login'),
    path('loginsave/', views.loginsave, name='loginsave'),
    path('Customer_login/', views.Customer_login, name='Customer_login'),
    path('logout/', views.llogout, name='logout')


    ]