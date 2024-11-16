from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class MovieListView(APIView):
    def get(self, request):
        movie_data = [
            {"id": "1234", "title": "The wild Robot", "date": "Sep 12, 2024", "poster": "https://media.themoviedb.org/t/p/w220_and_h330_face/wTnV3PCVW5O92JMrFvvrRcV39RU.jpg"},
            {"id": "34234", "title": "Terrifier 3", "date": "Oct 24, 2024", "poster": "https://media.themoviedb.org/t/p/w220_and_h330_face/63xYQj1BwRFielxsBDXvHIJyXVm.jpg"},
            {"id": "546546", "title": "Venom: The Last Dance", "date": "Nov 28, 2024", "poster": "https://media.themoviedb.org/t/p/w220_and_h330_face/k42Owka8v91trK1qMYwCQCNwJKr.jpg"},
            {"id": "3232423", "title": "The Substance", "date": "Oct 10, 2024", "poster": "https://media.themoviedb.org/t/p/w220_and_h330_face/lqoMzCcZYEFK729d6qzt349fB4o.jpg"}
        ]
        return Response(movie_data)
    
class NavbarView(APIView):
    def get(self, request):
        nav_item_list = [
            "Movies",
            "TV Shows",
            "People",
            "More"
        ]
        return Response(nav_item_list)