from rest_framework import serializers
from stack.models import Questions,Answer





class Answerserializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    question=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    # up_vote=serializers.CharField(read_only=True)
    up_vote_count=serializers.CharField(read_only=True)
    class Meta:
        model=Answer
        exclude=("up_vote",)
        # fields="__all__"


    def create(self, validated_data):
        question=self.context.get("question")
        user=self.context.get("user")
        return Answer.objects.create(user=user,question=question,**validated_data)


class Questionserializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    is_active=serializers.BooleanField(read_only=True)
    fetch_answer=Answerserializer(read_only=True,many=True)
    



    class Meta:
        model= Questions
        fields="__all__"