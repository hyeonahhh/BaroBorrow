from rest_framework.serializers import ModelSerializer
from .models import Product, BarrowProduct, Review, ReviewResult
from accounts.serializers import UserLikeSerializer, UserBasicSerializer
from rest_framework import serializers

#빌려주기
class ProductSerializer(ModelSerializer):
    owner = UserBasicSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'owner', 'product_name', 'list_price', 'deposit', 'rental_fee', 'explanation', 'condition', 'address', 'detail_address', 'product_photo', 'barrow_available_start', 'barrow_available_end', 'barrow_method']

class ProductLikeSerializer(ModelSerializer):
    like_users = UserLikeSerializer(read_only=True, many=True)
    owner = UserBasicSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'owner', 'product_name', 'like_users', 'list_price', 'deposit', 'rental_fee', 'explanation', 'condition', 'address', 'detail_address', 'product_photo', 'barrow_available_start', 'barrow_available_end', 'barrow_method']

#빌리기
class BarrowProductSerializer(ModelSerializer):
    
    user = UserBasicSerializer(required=False, read_only=True)
    product = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Product.objects.all()
    )
    class Meta:
        model = BarrowProduct
        fields = [
            'id', 'user', 'product', 'barrow_start', 'barrow_end', 'is_return', 'is_reviewed'
        ]
        #extra_kwargs = {"user": {"required": False, "allow_null": True}, "product": {"required": False, "allow_null": True}}


class ReviewSerializer(ModelSerializer):
    writer = UserBasicSerializer(required=False, read_only=True)
    barrow_product = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Product.objects.all(), required=False
    )
    trader = UserBasicSerializer(required=False, read_only=True)
    class Meta:
        model = Review
        fields = [
            'writer', 'barrow_product', 'trader', 'q_1', 'q_2', 'q_3', 'q_4', 'q_5'
        ]


class ReviewResultSerializer(ModelSerializer):
    user = UserBasicSerializer(required=False, read_only=True)
    class Meta:
        model = ReviewResult
        fields = [
            'user', 'av_q1', 'av_q2', 'av_q3', 'av_q4', 'av_q5'
        ]