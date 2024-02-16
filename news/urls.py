from django.urls import path
from .views import (
    PostView, PostDetail, PostSearch, PostCreate, PostEdit, PostDelete
)


urlpatterns = [
    path('', PostView.as_view(), name='posts'),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('search/', PostSearch.as_view(), name='search'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete')
]
