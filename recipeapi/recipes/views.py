from django.shortcuts import render
from recipes.models import Recipe,Review
from rest_framework.response import Response
from recipes.serializers import RecipeSerializer,UserSerializer,ReviewSerializer
from rest_framework import generics,viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework import status

class Recipelist(generics.ListCreateAPIView):     #non primary key based
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class Recipedetail(generics.RetrieveUpdateDestroyAPIView):   #primary key based
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Reviewlist(generics.ListCreateAPIView):     #non primary key based
    permission_classes =[IsAuthenticated,]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
class Reviewdetail(APIView):
    def get_object(self, request, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except:
            # return Response(Status=status.HTTP_404_NOT_FOUND)
            raise Http404
    def get(self, request, pk):
        recipes = self.get_object(request, pk)
        r = Review.objects.filter(recipe=recipes)  # retrieve product by category
        review = ReviewSerializer(r, many=True)
        return Response(review.data)
class search(APIView):
    def get(self,request):
        query=self.request.query_params.get('search')
        if(query):
            recipes = Recipe.objects.filter(Q(title__icontains=query) | Q(type__icontains=query))
            r=RecipeSerializer(recipes,many=True)
            return Response(r.data)

class user_logout(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        self.request.user.auth_token.delete()  #current user token deleted
        return Response(status=status.HTTP_200_OK)


