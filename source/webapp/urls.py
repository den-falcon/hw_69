from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from webapp.views import index_view, subtract_view, divide_view, add_view, multiply_view

urlpatterns = [
    path('', index_view, name='index'),
    path('add', add_view, name='add'),
    path('substract', subtract_view, name='substract'),
    path('divide', divide_view, name='divide'),
    path('multiply', multiply_view, name='multiply')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
