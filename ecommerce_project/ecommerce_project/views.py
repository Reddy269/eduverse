from django.http import JsonResponse


def _get_users(request):
    country = request.GET.get('country')
    age_min = request.GET.get('age_min')
    age_max = request.GET.get('age_max')

    try:
        age_min = int(age_min) if age_min else None
        age_max = int(age_max) if age_max else None
    except ValueError:
        return JsonResponse({'error': 'Invalid age filter'}, status=400)

    users = get_all_users(country=country, age_min=age_min, age_max=age_max)
    return JsonResponse({'count': len(users), 'users': users}, status=200)