from django.urls import path
from .views import HomeListViev,Post_detail,Post2_detail,MirListViev,Mir2_detail,Mir_detail

urlpatterns=[
     path('',HomeListViev.as_view(),name='home'),
     path('mir/',MirListViev.as_view(),name='mir'),
     path('post/<int:pk>',Post_detail.as_view(),name='post_detail'),
     path('post2/<int:pk>',Post2_detail.as_view(),name='post2_detail'),
     path('mir/<int:pk>',Mir_detail.as_view(),name='mir_detail'),
     path('mir2/<int:pk>',Mir2_detail.as_view(),name='mir2_detail'),
]