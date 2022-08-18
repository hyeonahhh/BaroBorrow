from rest_framework.serializers import ModelSerializer
from .models import Product, BarrowProduct
from accounts.serializers import UserLikeSerializer

#빌려주기
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'owner', 'product_name', 'list_price', 'deposit', 'rental_fee', 'explanation', 'condition', 'address', 'detail_address', 'product_photo', 'barrow_available_start', 'barrow_available_end']

class ProductLikeSerializer(ModelSerializer):
    like_users = UserLikeSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'like_users', 'list_price', 'deposit', 'rental_fee', 'explanation', 'condition', 'address', 'detail_address', 'product_photo', 'barrow_available_start', 'barrow_available_end']

#빌리기
class BarrowProductSerializer(ModelSerializer):
    class Meta:
        model = BarrowProduct
        fields = [
            'user', 'product', 'barrow_start', 'barrow_end', 'is_return'
        ]
