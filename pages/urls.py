from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

urlpatterns = [

    # path('',TemplateView.as_view(template_name="pages/index1.html")),
    path('',indexView.as_view()),
    # path('',form_index_view,name='form_index'),
    # path('',index),
    # path('exam/<str:username>/',csrf_exempt(viewExam.as_view()))
    path('exam/<str:username>/', viewListQuestions.as_view()),
    path('exam/<str:username>/<int:pk>/', viewQuestionDetail.as_view())
]
