from django.urls import path
from . import views
urlpatterns = [
    path('home',views.fn_home),
    path('login',views.fn_login),
    path('register',views.fn_register),
    path('menu',views.fn_menu),
    path('tower',views.fn_showtower), #for admin
    path('addtower',views.fn_addtower),
<<<<<<< HEAD
    path('viewtower',views.fn_viewtower), #for user
    path('showrack',views.fn_showrack), 
    path('addrack',views.fn_addrack),
    path('addbay',views.fn_addbay),
    path('showbay',views.fn_showbay), 
   
    path('logout',views.fn_logout),
    
]
=======
    path('viewtower',views.fn_viewtower),
    path('logout',views.fn_logout),
]
>>>>>>> 506fb80d47cfa378ec284df54bc027f2691247ca
