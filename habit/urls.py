from rest_framework.routers import DefaultRouter

from habit.views import HabitViewSet

app_name = 'habit'

router = DefaultRouter()
router.register(r'habit', HabitViewSet, basename='habit')

urlpatterns = [

              ] + router.urls
