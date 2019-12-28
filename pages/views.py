import json

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import Exam,Questions,User
from . import forms
from django.utils import timezone

def index(request):
    my_dict={'page_one_message':"This is a online quiz site"}
    return render(request,'pages/index.html',context=my_dict)

def form_index_view(request):
    form=forms.FormName()

    if request.method=='POST':
        form=forms.FormName(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            if len(User.objects.filter(username=username))>0 :
                return HttpResponseRedirect('exam/{0}'.format(username))
            else:
                message="no such username!"
                return render(request,'pages/form_name_page.html',{'form':form ,'message':message})

    return render(request,'pages/form_name_page.html',{'form':form})




class viewExam(View):

    def get(self,request,username):
        # 1)get the ids of questions in database
        # 2)create a list of qids
        # 3)select 20 non duplicated random  questions from this list
        # OR! use following code:)
        # question_list=[]
        userObj=User.objects.get(username=username)
        questions=Questions.objects.order_by('?')[0:5]
        exam=Exam(user=userObj,date=timezone.now(),answers='',score=0)

        exam.save()
        for q in questions:
            exam.questions.add(q)
        return render(request,"pages/exam_page.html",{'questions':questions,
                                                      'examid':exam.id})
    def post(self,request,username):
        json_obj=json.loads(request.body.decode("utf-8"))
        examid=json_obj['examid']
        exam=Exam.objects.get(id=int(examid))

        keys=[q.correct_choice_Id for q in exam.questions.all()]
        user_answers={}
        trues=0
        falses=0
        for answer in json_obj:
            if answer!='examid':
                user_answers[answer]=json_obj[answer]
        for i,key in enumerate(keys):
            if str(i+1) in user_answers:
                if int(user_answers[str(i+1)])==keys[i]:
                    trues+=1
                else:
                    falses+=1
        result=((3*trues-falses)*100)/(3*5)
        # save and send  result
        exam.answers=str(user_answers)
        exam.score=str(round(result,2))
        exam.save()
        return JsonResponse({"Your Score is" : str(round(result,2))})









