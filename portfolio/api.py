from rest_framework import filters, viewsets
from .models import Categoria
from .serializers import CategoriaSerializer

# Create your views here.
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.order_by('nombre')
    serializer_class = CategoriaSerializer