from django.shortcuts import render  # unused
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view  # unused
from .serializers import *
from .models import UsernameSnippet

from threads.models import Answer
from post.models import Channel, Question


class FrontPage(APIView):
	def get(self, request, cat, page):
		# cat = category
		# page = page number

		if not request.user.is_authenticated:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		order = "-" + cat
		page = int(page)
		mini = 10 * (page - 1)
		maxi = 10 * page

		if cat == "hot":
			posts = Question.objects.order_by("-hot")
		elif cat == "questions":
			posts = Question.objects.filter(
				metatype="question").order_by("-hot")
		elif cat == "unsolved":
			posts = Question.objects.filter(
				metatype="question", solved=False).order_by("-hot")
		elif cat == "discussions":
			posts = Question.objects.filter(
				metatype="discussion").order_by("-hot")
		posts = posts[mini:maxi]
		serializer = FPSerializer(posts, many=True)
		return Response(serializer.data)


class CheckUsername(APIView):
	def post(self, request):
		uname = request.data["username"]
		try:
			u = User.objects.get(username__iexact=uname)
			if u:
				snippet = UsernameSnippet(available=False)
				snippet.save()
				serializer = UsernameSerializer(snippet)
				return Response(serializer.data)
		except ObjectDoesNotExist:
			snippet = UsernameSnippet(available=True)
			snippet.save()
			serializer = UsernameSerializer(snippet)
			return Response(serializer.data)


class SuggestChannel(APIView):
	def post(self, request):
		text = request.data["text"]
		words = text.split()
		tag_names = [x.name for x in Channel.objects.all()]
		sugg_tag_names = [
			x for x in tag_names for y in words if x.lower() == y.lower()]
		sugg_tags = [Channel.objects.get(name=x) for x in sugg_tag_names]
		serializer = ChannelSerializer(sugg_tags, many=True)
		return Response(serializer.data)


class GetChannels(APIView):
	def get(self, request):
		tags = Channel.objects.all()
		serializer = ChannelSerializer(tags, many=True)
		return Response(serializer.data)

	def post(self, request):
		tags = Channel.objects.all()
		serializer = ChannelSerializer(tags, many=True)
		return Response(serializer.data)


class CreateChannel(APIView):
	def get(self, request):
		tags = Channel.objects.all()
		serializer = ChannelSerializer(tags, many=True)
		return Response(serializer.data)

	def post(self, request):
		ldata = {"name": request.data["name"].lower()}
		serializer = ChannelSerializer(data=ldata)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VotesView(APIView):

	def get(self, request):
		Answer.objects.score_update()
		answers = Answer.objects.order_by("-score")
		serializer = AnswerSerializer(answers, many=True)
		return Response(serializer.data)

		def post(self):
			pass


class AnswerVote(APIView):

	def GetAnswer(self, pk):
		try:
			return Answer.objects.get(pk=int(pk))
		except Answer.DoesNotExist:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def Vote(self, request, pk, ud):
		ans = self.GetAnswer(pk)
		if ud == 'u':
			vote_on = ans.ups
			vote_on_other = ans.downs
		elif ud == 'd':
			vote_on = ans.downs
			vote_on_other = ans.ups
		if request.user not in vote_on.all():
			vote_on.add(request.user)
			vote_on_other.remove(request.user)
		else:
			vote_on.remove(request.user)
		ans.set_score()
		ans.save()
		return ans

	def get(self, request, pk, ud):
		ans = self.Vote(request, pk, ud)
		serializer = AnswerSerializer(ans)
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	def post(self, request, pk, ud):
		pass


class QuestionVote(APIView):

	def GetQuestion(self, pk):
		try:
			return Question.objects.get(pk=int(pk))
		except Question.DoesNotExist:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def Vote(self, request, pk, ud):
		ques = self.GetQuestion(pk)
		if ud == 'u':
			vote_on = ques.ups
			vote_on_other = ques.downs
		elif ud == 'd':
			vote_on = ques.downs
			vote_on_other = ques.ups
		if request.user not in vote_on.all():
			vote_on.add(request.user)
			vote_on_other.remove(request.user)
		else:
			vote_on.remove(request.user)
		ques.points = ques.ups.count() - ques.downs.count()
		ques.save()
		return ques

	def get(self, request, pk, ud):
		ques = self.Vote(request, pk, ud)
		serializer = QuestionSerializer(ques)
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	def post(self, request, pk, ud):
		pass
