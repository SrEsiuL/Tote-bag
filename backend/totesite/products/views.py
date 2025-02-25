from django.http import JsonResponse
from .models import ToteBag
from django.http import HttpResponse

def totebag_list(request):
    totes = ToteBag.objects.all()
    data = [{"name": tote.name, "description": tote.description, "price": str(tote.price), "image": tote.image.url, "style": tote.style} for tote in totes]
    return JsonResponse(data, safe=False)


def home(request):
    return HttpResponse("¡Bienvenido a la página de Tote Bags!")

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Contact
import json

@csrf_exempt  # Permite solicitudes POST sin CSRF (solo para desarrollo)
def contact(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')

            if not name or not email or not message:
                return JsonResponse({'error': 'Todos los campos son requeridos'}, status=400)

            # Guardar el mensaje en la base de datos
            Contact.objects.create(name=name, email=email, message=message)
            return JsonResponse({'success': 'Mensaje enviado correctamente'}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)