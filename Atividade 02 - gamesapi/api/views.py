from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Game
from api.serializers import GameSerializer
from datetime import date

@api_view(['GET', 'POST'])
def game_list(request):
    if request.method == 'GET':
        games = Game.objects.all()
        games_serializer = GameSerializer(games, many=True)
        return Response(games_serializer.data)
    
    elif request.method == 'POST':
        games_serializer = GameSerializer(data=request.data)
        if games_serializer.is_valid():
            names = {game.name for game in Game.objects.all()}
            if request.data['name'] not in names:
                games_serializer.save()
                return Response(games_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'name': 'Name already exists'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(games_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def game_detail(request, pk):
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        game_serializer = GameSerializer(game)
        return Response(game_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        game_serializer = GameSerializer(game, data=request.data)
        if game_serializer.is_valid():
            names = {g.name for g in Game.objects.all()}
            if request.data['name'] not in names:
                game_serializer.save()
                return Response(game_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'name': 'Name already exists'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        if date.today() < game.release_date: 
            game.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'release_date': 'Game already released'}, status=status.HTTP_400_BAD_REQUEST)