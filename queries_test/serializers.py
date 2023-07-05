from rest_framework import serializers
from queries_test.models import student

class StudentSerializer(serializers.ModelSerializer):
  # def create(self, validated_data):
  #         # Handle the field and extract its value
  #         return student.objects.create(your_field=your_field_value, **validated_data)
  class Meta:
    model = student
    # fields = '__all__'

    fields = ["image" ,"name", "section", "age", "address","id"]
  extra_kwargs = {
        'id': {'read_only': True}
    }

