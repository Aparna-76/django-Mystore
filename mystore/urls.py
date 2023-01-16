from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import  DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
router=DefaultRouter()
router.register("api/products",views.ProductViewsetView,basename="products")
router.register("carts",views.CartsView,basename="carts")
router.register("users",views.UsersView,basename="users")
urlpatterns = [
    path('admin/', admin.site.urls),
    path("reviews/<int:pk>",views.ReviewDeleteView.as_view()),
    path("token/",obtain_auth_token),
    path("owner/",include("owner.urls")),
    path("",include("customer.urls"))
    # path("products",views.ProductView.as_view()),
    # path("products/<int:id>",views.ProductDetailsView.as_view())
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+router.urls
