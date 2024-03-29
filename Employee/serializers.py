from rest_framework import serializers
from Employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def validate_salary(self, value):
        if not (100000 >= value and value >= 25000):
            raise serializers.ValidationError(
                "salary should be in range of 25000 to 100000"
            )
        return value

    def validate(self, value):
        # jD = 2023 Td = 2025
        if value["joining_date"] > value["termination_date"]:
            raise serializers.ValidationError(
                "Joining date should be lesser than termination date"
            )
        return value
