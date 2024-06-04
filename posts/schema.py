import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from posts.models import Post
from users.schema import UserType

class PostType(DjangoObjectType):
    class Meta:
        model = Post


class Query(graphene.ObjectType):
    
    posts = graphene.List(
        PostType,
        id=graphene.Int(),
        postText=graphene.String(),
        created_at=graphene.DateTime(),
        
    )
    
    post = graphene.Field(PostType, id=graphene.Int())
    
    def resolve_posts(self, info, id=None, postText=None, created_at=None):
        filter_kwargs = {}
        if id is not None :
            filter_kwargs['id'] = id

        if postText is not None:
            filter_kwargs['postText__icontains'] = postText

        if created_at is not None:
            filter_kwargs['created_at__icontains'] = created_at

        if filter_kwargs:
            return Post.objects.filter(**filter_kwargs)
        else:
            return Post.objects.all()
    
    def resolve_post(self, info, id):
        try:
            return Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return None

class CreatePost(graphene.Mutation):

    id=graphene.Int()
    postUser=graphene.Field(UserType)
    postText=graphene.String()
    created_at=graphene.DateTime()
    postImage = graphene.String()

    class Arguments:
        postText=graphene.String()
        postImage = graphene.String()
        
    def mutate(self, info, postText=None,postImage=None):
        user = info.context.user or None
        if user.is_anonymous:
            #raise Exception('You must be logged to vote!')
            raise GraphQLError('GraphQLError: You must be logged to create post!')
        
        if postText is None and postImage is None:
            raise GraphQLError('GraphQLError: Either postText or postImage must be provided!')

        post = Post( 
                postText=postText,
                postImage=postImage,
                postUser=user,
                   )
        post.save()

        return CreatePost(
            id=post.id,
            postUser=post.postUser,
            postText=post.postText,
            created_at=post.created_at,
            postImage=post.postImage,
 
        )
    
class DeletePost(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        post_id = graphene.Int(required=True)

    def mutate(self, info, post_id):
        post = Post.objects.get(pk=post_id)
        post.delete()
        return DeletePost(id=post_id)


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    delete_post = DeletePost.Field()
