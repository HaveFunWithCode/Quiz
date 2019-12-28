from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',form_index_view,name='form_index'),
    # path('',index),
    path('exam/<str:username>/',csrf_exempt(viewExam.as_view())),
]
