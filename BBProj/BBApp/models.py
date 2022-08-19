from django.db import models
from accounts.models import User

# Create your models here.
class Product(models.Model):
    #빌려준 사람
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='myproducts', blank=True, null=True)
    #장바구니에 넣은 사람
    like_users = models.ManyToManyField(User, related_name='like_products', blank=True)
    #물품 이름
    product_name = models.CharField(max_length=256)
    #정가
    list_price = models.IntegerField()
    #보증금
    deposit = models.IntegerField()
    #대여비
    rental_fee = models.IntegerField()
    #설명
    explanation = models.TextField()
    #상태
    condition = models.IntegerField()
    #도로명주소
    address = models.TextField()
    #상세주소
    detail_address =  models.TextField()
    #사진
    product_photo = models.ImageField(blank=True, null=True, upload_to='product_photo')
    #대여가능기간 시작
    barrow_available_start = models.DateField()
    #대여가능기간 끝
    barrow_available_end = models.DateField()
    #대여 방식
    barrow_method = models.CharField(max_length=256)
    #활성화 비활성화
    is_activate = models.BooleanField(default=True)
    #대여중인지 아닌지
    is_barrowed = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name

class BarrowProduct(models.Model):
    #빌린 사람
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='myborrowproducts', blank=True, null=True)
    #물품 id
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='barrowed', blank=True, null=True)
    #빌리는 기간 시작
    barrow_start = models.DateField()
    #빌리는 기간 끝
    barrow_end = models.DateField()
    #반납되었는지 여부
    is_return = models.BooleanField(default=False)