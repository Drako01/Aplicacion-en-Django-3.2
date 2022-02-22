from django.shortcuts import render


def index(request):
    params = {}
    params["nombre_sitio"] = "LibrosOnline"
    return render(request, "vistaprevia/index.html", params)


def contacto(request):
    return render(request, "vistaprevia/contacto.html")
