from .models import Link
# Funcion para extender el diccionario de contextos

def context_dict(request):
    ctx = {}
    links = Link.objects.all()

    for link in links:
        ctx[link.key] = link.url
    return ctx