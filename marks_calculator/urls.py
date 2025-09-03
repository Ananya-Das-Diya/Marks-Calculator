from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('marks:dashboard')  # ✅ fix namespace
    return redirect('login')  # this will now point to /login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),   # /login, /logout, /register
    path('marks/', include(('marks.urls', 'marks'), namespace='marks')),  # namespaced
    path('', root_redirect, name="root_redirect"),  # root → dashboard or login
]
