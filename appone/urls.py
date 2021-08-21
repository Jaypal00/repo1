from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from appone.views import *

urlpatterns = [
    path('', home.as_view()),
    path('create/', StudCreate.as_view(), name='cr'),
    path('list/', login_required( StudList.as_view())),
    path('<pk>/detail/', login_required(StudDetailView.as_view())),
    path('<pk>/delete/',login_required (StudDeleteView.as_view())),
    path('<pk>/update', login_required(StudUpdateView.as_view())),
    path('search/', login_required(SearchView.as_view())),
    path('webscrap/', webscrap),
]