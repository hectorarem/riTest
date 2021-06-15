from rest_framework import serializers

from RocketTestApp.models import UserApp


class UserAppSerializer(serializers.ModelSerializer):
    phone = serializers.SerializerMethodField()
    class Meta:
        model = UserApp
        fields = [
            'uui',
            'last_login',
            'date_joined',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'phone',
        ]
    def get_phone(self, obj):
        return f"+{obj.phonePrefix}{obj.phone}" if obj.phonePrefix and obj.phone else None