# from blog.models import *
# from rest_framework import decorators
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .serializers import *
# @api_view(['POST'])
# def create__api(request):
#         data = request.data
#         title= data.get(title)
#         description = data['description']
#         release_date = data['release_date']
#         rating = data['rating']
#         serializer = AnimeSerializer(data)
#         if serializer.is_valid():
#             serializer.save() 
#             return Response('success')
#         else:
#             return Response(404)
# @api_view(['GET'])
# def rendeer__api(request):
#     postt = Anime.objects.all()
#     serializer = AnimeSerializer(postt, many=True)
#     return Response({"data" : serializer.data})
