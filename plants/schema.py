import graphene
from graphene_django import DjangoObjectType

from plants.models import Plant


class PlantType(DjangoObjectType):
    class Meta:
        model = Plant


class Query(graphene.ObjectType):
    plants = graphene.List(PlantType)

    def resolve_plants(self, info, **kwargs):
        return Plant.objects.all()

class CreatePlant(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    type = graphene.String()
    origin = graphene.String()
    description = graphene.String()
    image = graphene.String()

    class Arguments:
        name = graphene.String()
        type = graphene.String()
        origin = graphene.String()
        description = graphene.String()
        image = graphene.String()
        
    def mutate(self, info, name,type,origin, description,image):

        plant = Plant( name=name,
                      type=type,
                      origin=origin, 
                     description=description,
                     image=image,
                   )
        plant.save()

        return CreatePlant(
            id=plant.id,
            name=plant.name,
            type=plant.type,
            origin=plant.origin,
            description=plant.description,
            image=plant.image,
 
        )

class Mutation(graphene.ObjectType):
    create_plant = CreatePlant.Field()
