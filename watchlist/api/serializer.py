from rest_framework import serializers
from watchlist.models import WatchList, StreamPlatform


class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    # length_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"
        # or fields = ['id','name','description']
        # or exclude = ['active']

    # def get_length_name(self, object):
    #     return len(object.name)

    # def validate_name(self, value):  # field level validation
    #     if len(value) < 5:
    #         raise serializers.ValidationError("The name is too short")
    #     else:
    #         return value

    # def validate(self, object):  # object level validation
    #     if object['name'] == object['description']:
    #         raise serializers.ValidationError(
    #             "name and description should be different.")
    #     else:
    #         return object

# def description_length(value):
#     if len(value) < 10:
#         raise serializers.ValidationError("the description is too short")
#     return value


# class MovieSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(
#         validators=[description_length])  # validators
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate_name(self, value):  # field level validation
#         if len(value) < 5:
#             raise serializers.ValidationError("The name is too short")
#         else:
#             return value

#     def validate(self, movie):  # object level validation
#         if movie['name'] == movie['description']:
#             raise serializers.ValidationError(
#                 "name and description should be different.")
#         else:
#             return movie
