from rest_framework.serializers import ModelSerializer
from .models import Product, BarrowProduct

#빌려주기
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'owner', 'product_name', 'list_price', 'deposit', 'rental_fee', 'explanation', 'condition', 'address', 'detail_address', 'product_photo', 'barrow_available_start', 'barrow_available_end']

#빌리기
class BarrowProductSerializer(ModelSerializer):
    class Meta:
        model = BarrowProduct
        fields = ['barrowproduct_id', 'user', 'product', 'start_date', 'end_date', 'overdue_period', 'is_return']