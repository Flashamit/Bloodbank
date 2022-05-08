from django.urls import path
from .import views
urlpatterns = [
   
    path("home",views.home,name='home'),
    path('form',views.BForm.as_view(),name='form'),
    path('login',views.logins,name='login'),
    path('search',views.search,name='search'),
    path('donorlist',views.donorlist,name='donorlist'),
    path('donordata',views.donordata,name='donordata'),
    path('reciverdata',views.reciverdata,name='reciverdata'),
    path('reciverlist',views.reciverlist,name='reciverlist'),
    path('bbdetails',views.bloodbdetails,name='bbdetails'),
    path('donerform',views.DonerForm.as_view(),name='donerform'),
    path('complaint',views.ComplaintForm.as_view(),name='complaint'),
    path('complaintlist',views.complaintlist,name='complaintlist'),
    path('reciverform',views.ReciverForm.as_view(),name='reciverform'),
    path('updatebb/<int:pk>',views.UpdateBB.as_view(),name='updatebb'),
    path('deletebb/<int:pk>',views.DeleteBB.as_view(),name='deletebb'),
    path('register',views.Ragistration.as_view(),name='register'),
]
