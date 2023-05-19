from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from reviews.models import User

from reviews.models import Category, Comment, Genre, Review, Title


class RegisterDataSerializer(serializers.ModelSerializer):

    def validate_username(self, value):
        if value.lower() == "me":
            raise serializers.ValidationError("Username 'me' is not valid")
        return value

    class Meta:
        fields = ("username", "email")
        model = User


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()


class UserEditSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("username", "email", "first_name",
                  "last_name", "bio", "role")
        model = User
        read_only_fields = ('role',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("username", "email", "first_name",
                  "last_name", "bio", "role")
        model = User


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('__all__')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('__all__')


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = ('__all__')


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Review
        read_only_fields = ('title',)
        fields = ('id', 'text', 'author', 'score', 'pub_date')

    def create(self, validated_data):
        if Review.objects.filter(
            author=validated_data['author'],
            title=validated_data['title']
        ).exists():
            raise serializers.ValidationError(
                'Вы уже оставляли рецензию на это произведение'
            )
        return Review.objects.create(**validated_data)
    

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
