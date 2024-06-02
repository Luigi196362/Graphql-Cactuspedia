import graphene
from graphene_django import DjangoObjectType

from games.models import Game


class GameType(DjangoObjectType):
    class Meta:
        model = Game


class Query(graphene.ObjectType):
    games = graphene.List(
        GameType,
        id=graphene.Int(),
        gameName=graphene.String(),
        gameDescription=graphene.String(),
        
    )

    game = graphene.Field(GameType, id=graphene.String())

    def resolve_games(self, info, id=None, gameName=None, gameDescription=None):
        filter_kwargs = {}
        if id is not None :
            filter_kwargs['id'] = id

        if gameName is not None:
            filter_kwargs['gameName__icontains'] = gameName
            
        if gameDescription is not None:
            filter_kwargs['gameDescription__icontains'] = gameDescription

        if filter_kwargs:
            return Game.objects.filter(**filter_kwargs)
        else:
            return Game.objects.all()
        
    def resolve_game(self, info, id):
        try:
            return Game.objects.get(pk=id)
        except Game.DoesNotExist:
            return None


class CreateGame(graphene.Mutation):

    id=graphene.Int()
    gameName=graphene.String()
    gameDescription=graphene.String()
    gameIcon=graphene.String()
    gameImage=graphene.String()

    class Arguments:
        gameName = graphene.String()
        gameDescription = graphene.String()
        gameIcon = graphene.String()
        gameImage = graphene.String()
        
    def mutate(self, info, gameName,gameDescription,gameIcon,gameImage):

        game = Game( gameName=gameName,
                      gameDescription=gameDescription,
                      gameIcon=gameIcon, 
                      gameImage=gameImage,
                   )
        game.save()

        return CreateGame(
            id=game.id,
            gameName=game.gameName,
            gameDescription=game.gameDescription,
            gameIcon=game.gameIcon,
            gameImage=game.gameImage
 
        )
    
class DeleteGame(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        game_id = graphene.Int(required=True)

    def mutate(self, info, game_id):
        game = Game.objects.get(pk=game_id)
        game.delete()
        return DeleteGame(id=game_id)



class Mutation(graphene.ObjectType):
    create_game = CreateGame.Field()
    delete_game = DeleteGame.Field()
