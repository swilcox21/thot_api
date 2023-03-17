from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Reminder, Groop, Thot


class ReminderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    text = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    class Meta:
        model = Reminder
        fields = ['id','text','owner','due_date','recurring','completed','order']
    def update(self, instance, validated_data):
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.order = validated_data.get('order', instance.order)
        instance.recurring = validated_data.get('recurring', instance.recurring)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
    def create(self, validated_data):
        order = len(Reminder.objects.all())
        print("REMINDER:", order)
        return Reminder.objects.create(order=order + 1, **validated_data)

class _GroopSerializer(serializers.ModelSerializer): 
    owner = serializers.ReadOnlyField(source='owner.username')
    name = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    class Meta:                                 
        model = Groop
        fields = ['id','name','owner']
class _ThotSerializer(serializers.ModelSerializer): 
    class Meta:                                 
        model = Thot
        fields = ['id','text','dashboard','order']

class ThotSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    groop = _GroopSerializer(required=False)
    text = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    class Meta:
        model = Thot
        fields = ['id','text','created_date','dashboard','order','groop']   
    def update(self, instance, validated_data):
        instance.groop = validated_data.get('groop', instance.groop)
        instance.text = validated_data.get('text', instance.text)
        instance.order = validated_data.get('order', instance.order)
        instance.dashboard = validated_data.get('dashboard', instance.dashboard)
        instance.save()
        return instance
    def create(self, validated_data):
        order = len(Thot.objects.filter(groop=validated_data.get('groop')))
        return Thot.objects.create(order=order + 1, **validated_data)

class GroopSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    name = serializers.CharField(required=False, allow_blank=True, max_length=5000)
    thots = _ThotSerializer(many=True, required=False)
    class Meta:
        model = Groop
        fields = ['id','name','owner','home','hidden','order','image','thots']
    def update(self, instance, validated_data):
        instance.home = validated_data.get('home', instance.home)
        instance.hidden = validated_data.get('hidden', instance.hidden)
        instance.image = validated_data.get('image', instance.image)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    def create(self, validated_data):
        order = len(Groop.objects.all())
        return Groop.objects.create(order=order + 1,**validated_data)


class UserSerializer(serializers.ModelSerializer):
    reminders = ReminderSerializer(many=True, required=False)
    groops = GroopSerializer(many=True, required=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'reminders', 'groops']
