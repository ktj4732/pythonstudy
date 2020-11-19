from django.shortcuts import render, redirect
from .forms import RegisterForm
from user.models import User
from .models import Product
from django.http import Http404, HttpResponse
# Create your views here.




def delete(request, pk):
    product = Product.objects.get(pk=pk)

    product.delete()

    return redirect('/product/list')


def detail(request, pk):

    detail = {}

    try:
        product = Product.objects.get(pk=pk)

        detail['pk'] = product.id
        detail['name'] = product.name
        detail['img'] = product.productimg
        detail['price'] = product.price
        detail['description'] = product.description
        detail['reguser'] = product.reguser

        print('성공!')
        return render(request, 'productdetail.html', detail)

    except Product.DoesNotExist:
        HttpResponse('상품이없습니다.')


def register(request):

    if request.method == "POST":

        print('POST')

        print('form!')

        user_id = request.session.get('user')

        user = User.objects.get(pk=user_id)

        product = Product()

        product.name = request.POST.get('name', None)
        product.price = request.POST.get('price', None)
        product.description = request.POST.get('description', None)
        product.productimg = request.FILES.get('productimg', None)
        product.reguser = user

        product.save()
        print(product.productimg)
        print('저장완료!')

        return redirect('/product/list/')

    else:
        form = RegisterForm()
        print('등록화면')

    return render(request, 'register.html', {'form': form})


def list(request):
    all_product = Product.objects.all().order_by('id')

    return render(request, 'productlist.html', {'products': all_product})
