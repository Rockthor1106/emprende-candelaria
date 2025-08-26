from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from haztever.users.views import CustomConfirmEmailView

urlpatterns = [
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    path('admin/', admin.site.urls),
   
    path('users/', include('haztever.users.urls')),
    path('accounts/', include('allauth.urls')), 
    
    re_path(
        r"^api/auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$",
        CustomConfirmEmailView.as_view(),
        name="account_confirm_email",
    ),
    
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/business/', include('haztever.business.urls')),
    path('api/catalog/', include('haztever.catalog.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
]
