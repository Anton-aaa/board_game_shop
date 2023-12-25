from django.contrib import admin
from .models import (MyUser,
                     Goods,
                     Purchase,
                     ReturnGoods)

class MyUserAdmin(admin.ModelAdmin):
    fields = ('username',)

admin.site.register(MyUser, MyUserAdmin)


class GoodsAdmin(admin.ModelAdmin):
    fields = ('name',)

admin.site.register(Goods, GoodsAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    fields = ('purchase_quantity',)

admin.site.register(Purchase, PurchaseAdmin)


class ReturnGoodsAdmin(admin.ModelAdmin):
    fields = ('product',)

admin.site.register(ReturnGoods, ReturnGoodsAdmin)