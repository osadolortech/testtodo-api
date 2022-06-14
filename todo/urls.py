from rest_framework import routers
from .views import Todoviewset

router = routers.DefaultRouter()
router.register('todo',Todoviewset)