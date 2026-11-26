from rest_framework import filters, viewsets, generics, permissions
from .models import Categoria
from .serializers import CategoriaSerializer, RegistroSerializer, PerfilSerializer

# Create your views here.
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.order_by('nombre')
    serializer_class = CategoriaSerializer

class RegistroView(generics.CreateAPIView):
    serializer_class = RegistroSerializer
    permission_classes = [permissions.AllowAny]

class PerfilView(generics.RetrieveAPIView):
    serializer_class = PerfilSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user