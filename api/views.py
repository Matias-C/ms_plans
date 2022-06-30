from rest_framework.response import Response
from rest_framework.decorators import api_view
from discounts.models import Coupon
from .serializers import CouponSerializer

@api_view(['GET'])
def geData(request):
    coupons = Coupon.objects.all()
    serializer = CouponSerializer(coupons, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addCoupon(request):
    serializer = CouponSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)