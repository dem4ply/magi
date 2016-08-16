from rest_framework_nested import routers

from .views import Test as Test_view

router = routers.SimpleRouter()

router.register( r'test', Test_view, base_name='test' )

urlpatterns = router.urls
print( urlpatterns )
