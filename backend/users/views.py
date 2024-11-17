from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class TestView(APIView):
    def get(self, request):
        return Response("Hello, this is a test view in users app.")