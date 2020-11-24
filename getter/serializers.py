from rest_framework import serializers

class Serializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   id = serializers.IntegerField()
   course = serializers.IntegerField()
   time = serializers.DateTimeField()
