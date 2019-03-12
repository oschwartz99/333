from django.shortcuts import render

def default_map(request):
    return render(request, 'default.html', {'mapbox_access_token': 'pk.eyJ1IjoiY29zMzMzIiwiYSI6ImNqdDYzY3A0ZDBkMGc0YXF4azczdXRheWMifQ.3VeYeV_c-231Lab62H2XtQ'})