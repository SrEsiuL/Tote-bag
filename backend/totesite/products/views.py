from django.http import JsonResponse
from .models import ToteBag
from django.http import HttpResponse

def totebag_list(request):
    totes = ToteBag.objects.all()
    data = [{"name": tote.name, "description": tote.description, "price": str(tote.price), "image": tote.image.url, "style": tote.style} for tote in totes]
    return JsonResponse(data, safe=False)


def home(request):
    return HttpResponse("¡Bienvenido a la página de Tote Bags!")