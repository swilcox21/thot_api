from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly
from api.models import Reminder, Groop, Thot
from api.serializers import UserSerializer, ReminderSerializer, GroopSerializer, ThotSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.http import Http404
from django.shortcuts import get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class ReminderView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def get(self, request, reminder_id=None):
        print('request.data', self)
        if reminder_id is not None:
            reminder = get_object_or_404(Reminder.objects.all(), id = reminder_id)
            serialized_reminder = ReminderSerializer(reminder)
            return Response(serialized_reminder.data)
        all_reminders = Reminder.objects.filter(owner=request.user.id)
        serializer = ReminderSerializer(all_reminders, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ReminderSerializer(data=request.data, many=True)
        print('user', request.user)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        reminders = []
        for r in request.data:
            reminder = get_object_or_404(Reminder.objects.all(), id=r.get('id'))
            print('!!!!!USER:!!!!!!', r)
            ser_reminder = ReminderSerializer(instance=reminder, data=r, partial=True)
            print('!!!!!USER:!!!!!!', request)
            if ser_reminder.is_valid(raise_exception=True):
                ser_reminder.save()
            reminders.append(ser_reminder.data)
        return Response(reminders, status=status.HTTP_202_ACCEPTED)
    def delete(self,request,reminder_id):
        res = get_object_or_404(Reminder.objects.all(), id=reminder_id)
        reminder = get_object_or_404(Reminder.objects.all(), id=reminder_id)
        reminder.delete()
        return Response({"message": "reminder: `{}` has been deleted".format(res)}, status=status.HTTP_202_ACCEPTED)

class ThotView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def get(self, request, thot_id=None):
        print('request.data', Groop.objects.get(id=3).name)
        if thot_id is not None:
            thot = get_object_or_404(Thot.objects.all(), id = thot_id)
            serialized_thot = ThotSerializer(thot)
            return Response(serialized_thot.data)
        all_thots = Thot.objects.all()
        serializer = ThotSerializer(all_thots, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ThotSerializer(data=request.data, many=True)
        print('!!!!!USER:!!!!!!', request.data[0]['groop'])
        if serializer.is_valid():
            serializer.save(groop=Groop.objects.filter(id=request.data[0]['groop'].get('id')).first())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        thots = []
        for t in request.data:
            thot = get_object_or_404(Thot.objects.all(), id=t.get('id'))
            print('!!!!!USER:!!!!!!', t)
            ser_thot = ThotSerializer(instance=thot, data=t, partial=True)
            print('!!!!!USER:!!!!!!', request)
            if ser_thot.is_valid(raise_exception=True):
                ser_thot.save()
            thots.append(ser_thot.data)
        return Response(thots, status=status.HTTP_202_ACCEPTED)
    def delete(self,request):
        thots = []
        for t in request.data:
            thot = get_object_or_404(Thot.objects.all(), id=t.get('id'))
            thots.append(thot)
            thot.delete()
        return Response({"message": "thots: `{}` has been deleted".format(thots)}, status=status.HTTP_202_ACCEPTED)

class GroopView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def get(self, request, groop_id=None):
        print('request.data', self)
        if groop_id is not None:
            groop = get_object_or_404(Groop.objects.all(), id = groop_id)
            serialized_groop = GroopSerializer(groop)
            return Response(serialized_groop.data)
        all_groops = Groop.objects.filter(owner=request.user.id)
        serializer = GroopSerializer(all_groops, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = GroopSerializer(data=request.data, many=True)
        print('user', request.user)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        groops = []
        for f in request.data:
            groop = get_object_or_404(Groop.objects.all(), id=f.get('id'))
            print('!!!!!USER:!!!!!!', f)
            ser_groop = GroopSerializer(instance=groop, data=f, partial=True)
            print('!!!!!USER:!!!!!!', request)
            if ser_groop.is_valid(raise_exception=True):
                ser_groop.save()
            groops.append(ser_groop.data)
        return Response(groops.data, status=status.HTTP_202_ACCEPTED)
    def delete(self,request):
        groops = []
        for f in request.data:
            groop = get_object_or_404(Groop.objects.all(), id=f.get('id'))
            groops.append(groop)
            groop.delete()
        return Response({"message": "`{}` have been deleted".format(groops)},status=status.HTTP_202_ACCEPTED)
    # def put(self,request,groop_id):
    #     groop = get_object_or_404(Groop.objects.all(), id=groop_id)
    #     ser_groop = GroopSerializer(instance=groop, data=request.data, partial=True)
    #     if ser_groop.is_valid(raise_exception=True):
    #         ser_groop.save()
    #     return Response(ser_groop.data, status=204)
    # def delete(self,request,groop_id):
    #     groop_name = Groop.objects.get(id=groop_id).name
    #     groop = get_object_or_404(Groop.objects.all(), id=groop_id)
    #     groop.delete()
    #     return Response({"message": "groop: `{}` has been deleted".format(groop_name)},status=204)


