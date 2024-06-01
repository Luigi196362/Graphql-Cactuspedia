import graphene
from graphene_django import DjangoObjectType

from products.models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class Query(graphene.ObjectType):
    products = graphene.List(ProductType)

    def resolve_products(self, info, **kwargs):
        return Product.objects.all()

class CreateProduct(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    price = graphene.Int()
    stock = graphene.Int()
    description = graphene.String()
    image = graphene.String()

    class Arguments:
        name = graphene.String()
        price = graphene.Int()
        stock = graphene.Int()
        description = graphene.String()
        image = graphene.String()
        
    def mutate(self, info, name,price,stock, description,image):

        product = Product( name=name,
                      price=price,
                      stock=stock, 
                     description=description,
                     image=image,
                   )
        product.save()

        return CreateProduct(
            id=product.id,
            name=product.name,
            price=product.price,
            stock=product.stock,
            description=product.description,
            image=product.image,
 
        )






class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
