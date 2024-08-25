from rest_framework import viewsets
from .models import Artist, Artwork, Exhibition
from .serializers import ArtistSerializer, ArtworkSerializer, ExhibitionSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer

class ExhibitionViewSet(viewsets.ModelViewSet):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer