
from django.contrib import admin
from django.urls import path, include
from appone.views import *
from apptwo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', StudCreate.as_view(), name='cr'),
    # path('list/', StudList.as_view()),
    # path('<pk>/detail/', StudDetailView.as_view()),
    # path('<pk>/delete/', StudDeleteView.as_view()),
    # path('<pk>/update', StudUpdateView.as_view()),
    # path('search/', SearchView.as_view()),

    # path('signup/', signup),
    # path('login/', login),
    # path('logout/', logout),

    path('login/',user_login),
    path('signup/',sign_up),
    path('logout/',user_logout),
    # path('liststud/',stud_list),
    path('changepwd/',user_changepwd),
    path('',include('appone.urls'))

    # path('accounts/',include('django.contrib.auth.urls'))
]

