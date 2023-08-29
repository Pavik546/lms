from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from course.models import Program,Course
from base.models import Payment,Ymd
from accounts.models import Student

@csrf_exempt
def success(request,pk):
    payment =Payment()
    payment.student=request.user.id
    payment.course=pk
    payment.paid=True
    payment.save()

    return render(request, 'base/success.html')
   

def markview(request,str1,str2,pk,p,s,m):
    course=Course.objects.get(pk=pk)
    er=Ymd.objects.filter(student=request.user.username,courset=course.title,coursep=course.program,quizc=str2,quizt=str1).first()
    if not er:
        dude=Ymd()
        dude.student=request.user.username
        dude.courset=course.title
        dude.coursep=course.program
        dude.quizc=str2
        dude.quizt=str1   
        dude.total=p
        dude.score=s
        dude.maxscore=m
        dude.save()
        return HttpResponse(f"Your mark was added ,you scored {s} out of {m},Percentage={p}%")
    else:
        #return render(request, 'app/dashboard.html')
        return HttpResponse('You have already take this exam and only one sitting is permitted')

