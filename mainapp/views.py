from django.views.generic import TemplateView
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout as django_logout
from django.shortcuts import render ,redirect
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework import generics
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
User = get_user_model()


class RegisterView(generics.CreateAPIView):
	permission_classes = [AllowAny]
	serializer_class = UserSerializer
	queryset = User.objects.all()

	def create(self, request, *args, **kwarg):
		response = {}
		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid():
			serializer.save(password=make_password(request.data.get('password')))
			response['status'] = True
			response['msg'] = 'You have been registerd successfully. Now you can login your account.'
			return JsonResponse(response)
		else:
			try:
				message = list(serializer.errors.values())[0][0]
			except:
				message = "some error is occured please try again"
			response['status'] = False
			response['msg'] = message

			return JsonResponse(response)

class LoginView(generics.GenericAPIView):
	"""
	login view to login User
	"""
	permission_classes = [AllowAny]
	serializer_class = LoginSerializer
	queryset = User.objects.all()

	def post(self, request):
		response = {}
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		if username and password:
			try:
				user = authenticate(username=username, password=password)
			except Exception as e:
				response['status'] = False
				response['msg'] = str(e)
			else:
				if user:
					login(request, user)
					response['status'] = True
					response['data'] = UserSerializerList(instance=user).data
					response['msg'] = 'You have been login successfully.'
				else:
					response['status'] = False
					response['data'] = {}
					response['msg'] = 'Given credentials is wrong.'
		return JsonResponse(response)

class RegisterPageView(TemplateView):
	template_name = 'mainapp/register.html'
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('index')
		return render(request, self.template_name)

class LoginPageView(TemplateView):
	template_name = 'mainapp/login.html'
	def get(self, request):
		if request.user.is_authenticated:
				return redirect('index')
		return render(request, self.template_name)

class Index(LoginRequiredMixin,TemplateView):
	login_url = 'login-page'
	login_page = 'mainapp/index.html'
	def get(self, request, *args, **kwargs):
		return render(request, self.login_page)


class Logout(LoginRequiredMixin,TemplateView):
	login_url = 'login-page'
	login_page = 'mainapp/login.html'
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			django_logout(request)
			return redirect('login-page')
		return render(request, self.login_page)
