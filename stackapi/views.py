from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import authentication,permissions
from stackapi.serializers import Questionserializer,Answerserializer
from stack.models import Questions,Answer,User
from rest_framework.decorators import action
from rest_framework import mixins,generics
from stackapi.custompermissions import OwnerOrReadonly
from rest_framework import serializers



class Questionsview(viewsets.ModelViewSet):
    serializer_class=Questionserializer
    queryset=Questions.objects.all()
    # authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=["get","post","put"]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Questions.objects.all().exclude(user=self.request.user)


    @action(methods=["post"],detail=True)
    def add_answer(self,request,*args,**kw):
        question=self.get_object()
        user=request.user
        serializer=Answerserializer(data=request.data,context={"question":question,"user":user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class QuestionDeleteView( mixins.DestroyModelMixin,generics.GenericAPIView):

    queryset=Questions.objects.all()
    serializer_class=Questionserializer
    # authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[OwnerOrReadonly]
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class Answerview(viewsets.ViewSet):
    permission_classes=[permissions.IsAuthenticated,OwnerOrReadonly]
    # authentication_classes=[authentication.TokenAuthentication]
    @action(methods=["post"],detail=True)
    def add_up_vote(self,request,*args,**kw):
        id=kw.get("pk")
        answer=Answer.objects.get(id=id)
        user=request.user
        answer.up_vote.add(user)
        answer.save()
        return Response(data="you upvoted")


    def destroy(self,request,*args,**kw):
        id=kw.get("pk")
        object=Answer.objects.get(id=id)
        if object.user==request.user:
            Answer.objects.filter(id=id).delete()
            return Response(data="deleted")
        else:
            raise serializers.ValidationError("you donot have permissions")