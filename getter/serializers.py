from rest_framework import serializers

class Serializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   course = serializers.IntegerField()
   time = serializers.DateTimeField()
   id = serializers.IntegerField()