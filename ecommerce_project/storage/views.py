from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Customer


from storage.storages import CustomerStorage

@csrf_exempt
def register_customer_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.decoder.JSONDecodeError as e:
            return JsonResponse({'error, invalid json': str(e)}, status=400)
        try:
            customer = CustomerStorage.register_customer(data)
        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer does not exist'}, status=404)
        return JsonResponse({f"full_name: {customer.full_name}"}, status=201)


    return JsonResponse({'error': 'Method not allowed'}, status=405)

def user_detail(request,user_id):
    if request.method == 'GET':
        try:
            customer = Customer.objects.get(id = user_id)
        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer does not exist'}, status=404)

        return JsonResponse({
            'full_name': customer.full_name,
            'email': customer.email,
            'gender': customer.gender,
            'date_of_birth': customer.date_of_birth,
            'phone_number': customer.phone_number,
        })
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def user_create_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.decoder.JSONDecodeError as e:
            return JsonResponse({'error': str(e)}, status=400)



