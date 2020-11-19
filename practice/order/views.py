from django.shortcuts import render, redirect
from .models import Order
from product.models import Product
from user.models import User

# Create your views here.


def update(request, pk):

    productinfo = {}
    userinfo = {}

    user_id = request.session.get('user')

    user = User.objects.get(pk=user_id)
    order = Order.objects.get(pk=pk)

    if request.method == 'POST':

        order.quantity = request.POST.get('quantity')
        order.address = request.POST.get('address')
        order.price = int(order.countprice) * int(request.POST.get('quantity'))

        order.save()
        print('저장완료')

        return redirect('/order/detail/'+str(order.id))

    else:

        productinfo['productname'] = order.product
        productinfo['productprice'] = order.countprice
        productinfo['productreguser'] = order.userid
        productinfo['productimg'] = order.productimg
        userinfo['username'] = user.username
        userinfo['userid'] = user.userid

        print('주문수정화면')

        return render(request, 'orderupdate.html', {**userinfo, **productinfo})


def detail(request, pk):

    order = Order.objects.get(pk=pk)

    print(order.id)
    print(order.userid)
    print(order.price)

    return render(request, 'orderdetail.html', {'order': order})


def delete(request, pk):

    order = Order.objects.get(pk=pk)

    order.delete()

    print('삭제완료')

    return redirect('/order/list')


def orderPage(request, pk):

    productinfo = {}
    userinfo = {}

    user_id = request.session.get('user')

    user = User.objects.get(pk=user_id)
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':

        order = Order()

        order.user = user
        order.product = product
        order.userid = user.userid
        order.quantity = request.POST.get('quantity')
        order.address = request.POST.get('address')
        order.productimg = product.productimg
        order.countprice = product.price
        order.price = int(product.price) * int(request.POST.get('quantity'))

        order.save()
        print('저장완료')

        return redirect('/order/list/')

    else:

        productinfo['productname'] = product.name
        productinfo['productprice'] = product.price
        productinfo['productreguser'] = product.reguser
        productinfo['productimg'] = product.productimg
        userinfo['username'] = user.username
        userinfo['userid'] = user.userid

        print('주문화면')

        return render(request, 'orderpage.html', {**userinfo, **productinfo})


def orderList(request):

    # 로그인중인 아이디
    user_id = request.session.get('user')

    user = User.objects.get(pk=user_id)

    print(user)

    # 로그인한 아이디의 주문내역
    orders = Order.objects.filter(userid=user)

    # print(orders.user)

    return render(request, 'orderlist.html', {'orders': orders})
