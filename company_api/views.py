
from django.http import HttpResponse, JsonResponse




def home_page(request):
    print("Home page requested")
    sangat=[
        'Hunain',
        'Khareen',
        'Saqib'
    ]
    return JsonResponse(sangat,safe=False) 