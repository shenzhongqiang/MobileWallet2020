from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.db import transaction
from .models import User, Transaction, Usage
from .decorators import record_usage
import json

# Create your views here.
@csrf_exempt
def login_user(request):
    if request.method == "GET":
        return render(request, 'login.html')

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            result = {
                "success": True,
                "message": "successfully logged in"
            }
            return JsonResponse(result)
        else:
            result = {
                "success": False,
                "message": "invalid username or password"
            }
            return JsonResponse(result)

def logout_user(request):
    logout(request)
    result = {
        "success": True,
        "message": "successfully logged out"
    }
    return JsonResponse(result)

@record_usage
def list_users(request):
    user_objs = User.objects.all()
    users = []
    for user in user_objs:
        users.append({
            "id": user.id,
            "username": user.username,
            "balance": user.balance
        })

    result = {
        "success": True,
        "message": "",
        "data": {
            "users": users
        }
    }
    return JsonResponse(result)

@login_required
def list_usages(request):
    usage_objs = Usage.objects.all()
    usages = []
    for usage in usage_objs:
        usages.append({
            "id": usage.id,
            "api_name": usage.api_name,
            "username": usage.user.username,
            "timestamp": usage.timestamp
        })
    result = {
        "success": True,
        "message": "",
        "data": {
            "usages": usages
        }
    }
    return JsonResponse(result)

@csrf_exempt
@login_required
@record_usage
def deposit(request):
    if request.method == "GET":
        context = {"username": request.user.username}
        return render(request, "deposit.html", context)

    if request.method == "POST":
        user = request.user
        amount = request.POST.get("amount")
        try:
            amount = float(amount)
        except:
            result = {
                "success": False,
                "message": "invalid amount"
            }
            return JsonResponse(result)
        user.balance += amount
        user.save()
        result = {
            "success": True,
            "message": "successfully added money"
        }
        return JsonResponse(result)

@login_required
@record_usage
def get_balance(request):
    user = request.user
    balance = user.balance
    result = {
        "success": True,
        "message": "",
        "data": {
            "balance": balance
        }
    }
    return JsonResponse(result)

@login_required
@record_usage
def get_user_transactions(request):
    user = request.user
    my_sent = user.my_sent.all()
    my_received = user.my_received.all()
    sent_transacs = []
    for transac in my_sent:
        sent_transacs.append({
            "id": transac.id,
            "to_user": transac.to_user.username,
            "amount": transac.amount,
            "timestamp": transac.timestamp
        })
    received_transacs = []
    for transac in my_received:
        received_transacs.append({
            "id": transac.id,
            "from_user": transac.from_user.username,
            "amount": transac.amount,
            "timestamp": transac.timestamp
        })
    result = {
        "success": True,
        "message": "",
        "data": {
            "sent_transactions": sent_transacs,
            "received_transactions": received_transacs
        }
    }
    return JsonResponse(result)

@login_required
@record_usage
def get_all_transactions(request):
    transac_objs = Transaction.objects.all()
    transacs = []
    for transac in transac_objs:
        transacs.append({
            "id": transac.id,
            "from_user": transac.from_user.username,
            "to_user": transac.to_user.username,
            "amount": transac.amount,
            "timestamp": transac.timestamp,
        })
    result = {
        "success": True,
        "message": "",
        "data": {
            "transactions": transacs,
        }
    }
    return JsonResponse(result)

@csrf_exempt
@login_required
@transaction.atomic
@record_usage
def transfer(request):
    if request.method == "GET":
        context = {"username": request.user.username}
        return render(request, 'transfer.html', context)

    if request.method == "POST":
        from_user = request.user
        to_username = request.POST.get("to")
        if from_user.username == to_username:
            result = {
                "success": False,
                "message": "cannot transfer money to yourself"
            }
            return JsonResponse(result)

        amount = request.POST.get("amount")
        try:
            to_user = User.objects.get(username=to_username)
        except User.DoesNotExist:
            result = {
                "success": False,
                "message": "user {} does not exist".format(to_username),
            }
            return JsonResponse(result)

        try:
            amount = float(amount)
        except:
            result = {
                "success": False,
                "message": "amount {} is not a valid amount".format(amount),
            }

        if from_user.balance < amount:
            result = {
                "success": False,
                "message": "not enough money to transfer"
            }
            return JsonResponse(result)

        from_user.balance -= amount
        to_user.balance += amount
        transac = Transaction(from_user=from_user, to_user=to_user, amount=amount)
        from_user.save()
        to_user.save()
        transac.save()
        result = {
            "success": True,
            "message": "successfully transfered money"
        }
        return JsonResponse(result)

