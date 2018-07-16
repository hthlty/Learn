#coding=utf-8


#购物车
# 1.可以向购物车中添加商品，可以设置数量
# 2.可以删除购物车中商品，包括减少数量
# 3.允许清空购物车
# 4.每次操作完重新统计商品总金额（商品总金额=商品价格*商品数量）

shoppingcart = {}

def totalprice():
    global shoppingcart
    sumprice = 0
    for k,v in shoppingcart.items():
        sumprice += v['price']*v['num']
    return sumprice

def goods_add(gid,name,price,num):
    global shoppingcart
    if gid not in shoppingcart:
        shoppingcart[gid] = {'gid':gid,'name':name,'price':price,'num':num}
    else:
        shoppingcart[gid]['num'] +=num
    print(totalprice())
    print(shoppingcart)

def goods_del(gid,num):
    global shoppingcart
    if gid not in shoppingcart:
        return False
    if shoppingcart[gid]['num'] > num:
        shoppingcart[gid]['num'] -=num
    else:
        shoppingcart.pop(gid)
    print(totalprice())
    print(shoppingcart)

def goods_clear():
    global shoppingcart
    shoppingcart.clear()
    print(shoppingcart)

goods_add(1,'牛奶',10,3)
goods_add(2,'香蕉',8,4)
goods_add(3,'鸡蛋',2,10)
goods_add(1,'牛奶',10,6)
goods_del(2,2)
goods_clear()