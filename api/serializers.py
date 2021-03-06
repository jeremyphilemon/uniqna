from rest_framework import serializers
from .models import UsernameSnippet

from post.models import Channel, Question
from threads.models import Answer


class AnswerSerializer(serializers.ModelSerializer):
	ups = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	downs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = Answer
		fields = ("id", "ups", "downs", "points")


class QuestionSerializer(serializers.ModelSerializer):
	ups = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	downs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = Question
		fields = ("id", "ups", "downs", "points")


class ChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Channel
		fields = '__all__'


class UsernameSerializer(serializers.ModelSerializer):
	class Meta:
		model = UsernameSnippet
		fields = '__all__'
