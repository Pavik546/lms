from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt


def pay(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 5000

        client = razorpay.Client(
            auth=("rzp_test_QFAMTYWLcA390R", "MEQd19Z0QdVgcn407Tj2dAmQ"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'base/index.html')

@csrf_exempt
def success(request):
    return render(request, "base/success.html")
