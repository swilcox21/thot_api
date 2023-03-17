# from unicodedata import name
from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, ReminderView, GroopView, ThotView

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('reminder/', ReminderView.as_view()),
    path('reminder/<int:reminder_id>', ReminderView.as_view()),
    path('groop/', GroopView.as_view()),
    path('groop/<int:groop_id>', GroopView.as_view()),
    path('thot/', ThotView.as_view()),
    path('thot/<int:thot_id>', ThotView.as_view()),
]