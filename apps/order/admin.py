from django.contrib import admin

from order.models import OrderGoods,OrderInfo

admin.site.register(OrderGoods)
admin.site.register(OrderInfo)
