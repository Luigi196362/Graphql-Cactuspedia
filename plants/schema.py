import graphene
from graphene_django import DjangoObjectType

from plants.models import Plant


class PlantType(DjangoObjectType):
    class Meta:
        model = Plant


class Query(graphene.ObjectType):
    plants = graphene.List(
        PlantType,
        id=graphene.Int(),
        plantName=graphene.String(),
        plantType=graphene.String(),
        plantOrigin=graphene.String(),
        plantDescription=graphene.String()  
        
    )

    plant = graphene.Field(PlantType, id=graphene.Int())

    def resolve_plants(self, info, id=None, plantName=None, plantType=None, plantOrigin=None, plantDescription=None):
        filter_kwargs = {}
        if id is not None :
            filter_kwargs['id'] = id

        if plantName is not None:
            filter_kwargs['plantName__icontains'] = plantName

        if plantType is not None:
            filter_kwargs['plantType__icontains'] = plantType

        if plantOrigin is not None:
            filter_kwargs['plantOrigin__icontains'] = plantOrigin

        if plantDescription is not None:
            filter_kwargs['plantDescription__icontains'] = plantDescription

        if filter_kwargs:
            return Plant.objects.filter(**filter_kwargs)
        else:
            return Plant.objects.all()
        
    def resolve_plant(self, info, id):
        try:
            return Plant.objects.get(pk=id)
        except Plant.DoesNotExist:
            return None


class CreatePlant(graphene.Mutation):

    id = graphene.Int()
    plantName = graphene.String()
    plantType = graphene.String()
    plantOrigin = graphene.String()
    plantDescription = graphene.String()
    plantImage = graphene.String()

    class Arguments:
        plantName = graphene.String()
        plantType = graphene.String()
        plantOrigin = graphene.String()
        plantDescription = graphene.String()
        plantImage = graphene.String()
        
    def mutate(self, info, plantName,plantType,plantOrigin, plantDescription,plantImage):

        plant = Plant( plantName=plantName,
                      plantType=plantType,
                      plantOrigin=plantOrigin, 
                      plantDescription=plantDescription,
                      plantImage=plantImage,
                   )
        plant.save()

        return CreatePlant(
            id=plant.id,
            plantName=plant.plantName,
            plantType=plant.plantType,
            plantOrigin=plant.plantOrigin,
            plantDescription=plant.plantDescription,
            plantImage=plant.plantImage,
 
        )
    
class DeletePlant(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        plant_id = graphene.Int(required=True)

    def mutate(self, info, plant_id):
        plant = Plant.objects.get(pk=plant_id)
        plant.delete()
        return DeletePlant(id=plant_id)


class Mutation(graphene.ObjectType):
    create_plant = CreatePlant.Field()
    delete_plant = DeletePlant.Field()
