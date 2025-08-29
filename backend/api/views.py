from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Club
from .serializers import ClubSerializer

class ClubCreate(generics.ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

# Retrieve, update, or delete a specific Club
class ClubDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer