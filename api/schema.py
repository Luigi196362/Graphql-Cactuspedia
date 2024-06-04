import graphene
import graphql_jwt
import products.schema
import plants.schema
import users.schema
import games.schema
import posts.schema

class Query(users.schema.Query, 
            products.schema.Query,
            plants.schema.Query, 
            games.schema.Query,
            posts.schema.Query,
            graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation,
               products.schema.Mutation,
               plants.schema.Mutation,
               games.schema.Mutation,
               posts.schema.Mutation,
               graphene.ObjectType):
    
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)