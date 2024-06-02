import graphene
from graphene_django import DjangoObjectType

from products.models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class Query(graphene.ObjectType):
    products = graphene.List(
        ProductType,
        id=graphene.Int(),
        productName=graphene.String(),
        productPrice=graphene.Int(),
        productStock=graphene.Int(),
        productDescription=graphene.String(),
        
    )

    product = graphene.Field(ProductType, id=graphene.Int())

    def resolve_products(self, info, id=None, productName=None, productPrice=None, productStock=None, productDescription=None):
        filter_kwargs = {}
        if id is not None :
            filter_kwargs['id'] = id

        if productName is not None:
            filter_kwargs['productName__icontains'] = productName

        if productPrice is not None:
            filter_kwargs['productPrice__icontains'] = productPrice

        if productStock is not None:
            filter_kwargs['productStock__icontains'] = productStock

        if productDescription is not None:
            filter_kwargs['productDescription__icontains'] = productDescription

        if filter_kwargs:
            return Product.objects.filter(**filter_kwargs)
        else:
            return Product.objects.all()
        
    def resolve_product(self, info, id):
        try:
            return Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return None


class CreateProduct(graphene.Mutation):

    id=graphene.Int()
    productName=graphene.String()
    productPrice=graphene.Int()
    productStock=graphene.Int()
    productDescription=graphene.String()
    productImage=graphene.String()

    class Arguments:
        productName = graphene.String()
        productPrice = graphene.Int()
        productStock = graphene.Int()
        productDescription = graphene.String()
        productImage = graphene.String()
        
    def mutate(self, info, productName,productPrice,productStock, productDescription,productImage):

        product = Product( productName=productName,
                      productPrice=productPrice,
                      productStock=productStock, 
                      productDescription=productDescription,
                      productImage=productImage,
                   )
        product.save()

        return CreateProduct(
            id=product.id,
            productName=product.productName,
            productPrice=product.productPrice,
            productStock=product.productStock,
            productDescription=product.productDescription,
            productImage=product.productImage,
 
        )
    
class DeleteProduct(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        product_id = graphene.Int(required=True)

    def mutate(self, info, product_id):
        product = Product.objects.get(pk=product_id)
        product.delete()
        return DeleteProduct(id=product_id)



class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    delete_product = DeleteProduct.Field()
