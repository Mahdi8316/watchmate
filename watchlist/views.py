# from django.shortcuts import render
# from watchlist.models import Movie
# from django.http import JsonResponse


# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         'all movies': list(movies.values())
#     }
#     return JsonResponse(data)


# def particular_movie(request, id):
#     movie = Movie.objects.get(pk=id)
#     data = {
#         'name': movie.name,
#         'description': movie.description,
#         'active': movie.active
#     }
#     return JsonResponse(data)
