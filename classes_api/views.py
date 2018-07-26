from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from classes.models import Classroom
from .serializers import ListSerializer, DetailSerializer, ClassroomCreateUpdateSerializer

# Create your views here.

class List(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ListSerializer

class Detail(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = DetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


class Create (CreateAPIView):
	serializer_class = ClassroomCreateUpdateSerializer
	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)
		#assigning teacher automatically as the object is being written 
		#override the class of create


class Update (RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomCreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'



class Delete(DestroyAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'


