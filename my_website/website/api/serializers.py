from rest_framework.serializers import ModelSerializer
from website.models import Member


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        
#for the fields, you can make a list of what you want to return instead of returning all, for example
# fields = ['id', 'firstname', 'lastname', 'language']