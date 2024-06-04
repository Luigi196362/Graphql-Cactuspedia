import graphene
from graphene_django import DjangoObjectType

from users.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = User(
            username=username,
            email=email,

        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    is_premium = graphene.Boolean()
    is_admin = graphene.Boolean()

    def resolve_users(self, info):
        return User.objects.all()
    
    def resolve_is_premium(self, info):
        user = info.context.user
        if user.is_authenticated:
            
            return user.is_premium
        return user.is_premium
    
    def resolve_is_admin(self, info):
        user = info.context.user
        if user.is_authenticated:
            
            return user.is_admin
        return user.is_admin