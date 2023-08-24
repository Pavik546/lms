from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from course.models import Program
from base.models import Payment
from accounts.models import Student
@csrf_exempt
def success(request,pk):
    payment =Payment()
    payment.student=request.user.id
    payment.course=pk
    payment.paid=True
    payment.save()

    return render(request, 'base/success.html')
