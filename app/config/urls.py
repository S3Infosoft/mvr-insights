from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("schedule/", include("schedules.urls", namespace="schedule")),
    path("accounts/", include("allauth.urls")),
    path("activity/", include("activities.urls", namespace="activity")),
    path("enquiry/", include("enquiry.urls", namespace="enquiry")),
    path('admin/', admin.site.urls),
    path("api/v1/", include("apis.urls")),
    path("", include("users.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
