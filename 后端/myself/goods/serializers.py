from rest_framework import serializers
from .models import goods, favorite, order, Comment, replay,goods_type
from users.serializers import UserSerializer

class goodSerializer(serializers.ModelSerializer):
    class Meta:
        model = goods
        fields = ('__all__')

class goodCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = goods
        fields = ('__all__')
    def create(self, validated_data):
        return goods.objects.create(**validated_data)

class GoodUpdateSerializer(goodSerializer):
    id = serializers.IntegerField(required=True)
    good_name = serializers.CharField(required=False)
    good_price = serializers.IntegerField(required=False)
    good_brand = serializers.CharField(required=False)
    good_content = serializers.CharField(required=False)
    good_img = serializers.ImageField(required=False)
    good_num = serializers.IntegerField(required=False)

    def update(self, instance, validated_data):
        instance.good_name = validated_data.get('good_name', instance.good_name)
        instance.good_price = validated_data.get('good_price', instance.good_price)
        instance.good_brand = validated_data.get('good_brand', instance.good_brand)
        instance.good_content = validated_data.get('good_content', instance.good_content)
        instance.good_img = validated_data.get('good_img', instance.good_img)
        instance.good_num = validated_data.get('good_num', instance.good_num)
        instance.save()
        return instance

class FavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    good = goodSerializer()

    class Meta:
        model = favorite
        fields = ('__all__')

class FavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = favorite
        fields = ('__all__')
    def create(self, validated_data):
        return favorite.objects.create(**validated_data)

class FavoriteUpdateSerializer(FavoriteCreateSerializer):
    good_num = serializers.IntegerField(required=True)

    def update(self, instance, validated_data):
        instance.good_num = validated_data.get('good_num', instance.good_num)
        instance.save()
        return instance

class orderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    good = goodSerializer()
    class Meta:
        model = order
        fields = ('__all__')


class orderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = ('__all__')

    def create(self, validated_data):
        return order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.good_num = validated_data.get('good_num', instance.good_num)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    good = goodSerializer()
    comment_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Comment
        fields = ('__all__')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class ReplaySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    comment = CommentSerializer()

    class Meta:
        model = replay
        fields = ('__all__')


class ReplayCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = replay
        fields = ('__all__')

    def create(self, validated_data):
        return replay.objects.create(**validated_data)

class GoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = goods_type
        fields = ('__all__')