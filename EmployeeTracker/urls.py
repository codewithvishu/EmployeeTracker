from django.contrib import admin
from django.urls import path, include


from django.http import JsonResponse

def healthcheck(request):
    return JsonResponse({"Status":"Up"}, status=200)

urlpatterns = [
    path('healthcheck/',healthcheck),
    path('admin/', admin.site.urls),
    path('api/v1/', include('Employee.urls')),
]