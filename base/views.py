from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from course.models import Program


def pay(request,pk,fee):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 5000


        client = razorpay.Client(
            auth=("rzp_test_QFAMTYWLcA390R", "MEQd19Z0QdVgcn407Tj2dAmQ"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'base/index.html',{'programid':pk,'programfees':fee*100})




    # Rest of your view logic

