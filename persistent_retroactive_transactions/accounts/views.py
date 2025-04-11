from django.shortcuts import render
from django.http import HttpResponse
from .persistent_retroactivity import PersistentRetroactiveAccountSystem

account_system = PersistentRetroactiveAccountSystem()

def home(request):
    return render(request, 'accounts/home.html')

def create_account(request):
    if request.method == "GET" and "name" in request.GET:
        name = request.GET.get("name")
        balance = int(request.GET.get("balance", 0))
        timestamp = request.GET.get("timestamp")
        timestamp = int(timestamp) if timestamp else None

        success = account_system.create_account(name, balance, timestamp)

        if success:
            return render(request, "accounts/result.html", {
                "message": f"Account '{name}' created with balance {balance}."
            })
        else:
            return render(request, "accounts/result.html", {
                "message": f"Account '{name}' already exists."
            })
    return render(request, 'accounts/create_account.html')

def deposit(request):
    if request.method == "GET" and "name" in request.GET:
        name = request.GET.get("name")
        amount = int(request.GET.get("amount", 0))
        timestamp = request.GET.get("timestamp")
        timestamp = int(timestamp) if timestamp else None

        success = account_system.deposit(name, amount, timestamp)
        if success:
            return render(request, "accounts/result.html", {
                "message": f"Deposited {amount} to '{name}'"
            })
        else:
            return render(request, "accounts/result.html", {
                "message": f"Account '{name}' does not exist."
            })
    return render(request, 'accounts/deposit.html')

def withdraw(request):
    if request.method == "GET" and "name" in request.GET:
        name = request.GET.get("name")
        amount = int(request.GET.get("amount", 0))
        timestamp = request.GET.get("timestamp")
        timestamp = int(timestamp) if timestamp else None

        success = account_system.withdraw(name, amount, timestamp)
        if success:
            return render(request, "accounts/result.html", {
                "message": f"Withdrew {amount} from '{name}'"
            })
        else:
            return render(request, "accounts/result.html", {
                "message": f"Insufficient funds or account '{name}' does not exist."
            })
    return render(request, 'accounts/withdraw.html')

def transfer(request):
    if request.method == "GET" and "sender" in request.GET:
        sender_name = request.GET.get("sender")
        receiver_name = request.GET.get("receiver")
        amount = int(request.GET.get("amount", 0))
        timestamp = request.GET.get("timestamp")
        timestamp = int(timestamp) if timestamp else None

        success = account_system.transfer(sender_name, receiver_name, amount, timestamp)
        if success:
            return render(request, "accounts/result.html", {
                "message": f"Transferred {amount} from '{sender_name}' to '{receiver_name}'."
            })
        else:
            return render(request, "accounts/result.html", {
                "message": "Transfer failed due to insufficient funds or non-existing account."
            })

    return render(request, 'accounts/transfer.html')

def rollback(request):
    if request.method == "GET" and "timestamp" in request.GET:
        try:
            timestamp = int(request.GET.get("timestamp"))
            operation_type = request.GET.get("operation_type")
        except (TypeError, ValueError):
            return render(request, "accounts/result.html", {
                "message": "Invalid timestamp or operation type.",
                "home_link": True
            })

        success = account_system.rollback(timestamp, operation_type)
        if success:
            return render(request, "accounts/result.html", {
                "message": f"Rolled back '{operation_type}' at timestamp {timestamp}.",
                "home_link": True
            })
        else:
            return render(request, "accounts/result.html", {
                "message": f"No matching '{operation_type}' operation found at timestamp {timestamp}.",
                "home_link": True
            })

    return render(request, 'accounts/rollback.html')


def view_balances(request):
    version = request.GET.get("version")
    try:
        version_int = int(version) if version else account_system.max_time
    except ValueError:
        version_int = account_system.max_time

    balances = []
    for name in account_system.get_all_accounts().keys():
        balance = account_system.get_balance(name, version_int)
        balances.append({
            "name": name,
            "balance": balance,
            "version": version_int
        })

    return render(request, "accounts/view_balances.html", {
        "balances": balances,
        "version": version_int
    })
