from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm
from board.models import Board
from product.models import Product
from order.models import Order

# Create your views here.


# 내정보(my info)
def myinfo(request):

    user_id = request.session.get('user')

    userinfo = {}

    if user_id:

        user = User.objects.get(pk=user_id)

        userinfo['userid'] = user.userid
        userinfo['username'] = user.username
        userinfo['useremail'] = user.useremail
        userinfo['userregdate'] = user.regdate
        userinfo['userimg'] = user.userimg

        order = Order.objects.filter(userid=user)

        orders = {}

        orders['order'] = order

        product = Product.objects.filter(reguser=user)

        products = {}

        products['product'] = product

        return render(request, 'myinfo.html', {**userinfo, **orders, **products})
    else:

        return redirect('/user/login/')
 # home 함수


def home(request):
    # 현재 로그인된 세션값을 가져와 user_id에 저장
    user_id = request.session.get('user')
    userinfo = {}
    boardinfo = {}

    board = Board.objects.all()

    boardinfo['board'] = board
    # user_id가 존재 할경우
    if user_id:
        print('세션가져오기 성공')

        # 로그인 세션값과 같은 pk를 가지는 정보들을 가져온다.
        user = User.objects.get(pk=user_id)

        # useroinfo라는 딕셔러니에 불러오고 싶은 값들을 넣어준다
        userinfo['username'] = user.username
        userinfo['useremail'] = user.useremail
        userinfo['userimg'] = user.userimg

        product = Product.objects.all()

        products = {}

        products['product'] = product

    # 해당 템플릿에 정보들을 보내준다.
    return render(request, 'home.html', {**userinfo, **boardinfo, **products})

# 회원가입


def signup(request):

    # method가 GET 방식일 경우 회원가입을 할 수 있는 화면을 나타내준다
    if request.method == 'GET':
        return render(request, 'signup.html')

    # method가 POST일 경우 회원가입 내용들을 모두 작성하고 회원가입을 시도하는 것이기
    # 때문에 유효성 검사를 통과하면 데이터들을 저장해준다.
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        userid = request.POST.get('userid', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        useremail = request.POST.get('useremail', None)
        userimg = request.FILES.get('userimg', None)

        # 유효성 검사시 에러메세지들을 담을 딕셔너리 생성
        errormessage = {}

        # 유효성 검사
        if not (username and userid and password and repassword):
            errormessage['error'] = '모든값을 입력해야합니다.'

            return render(request, 'signup.html', errormessage)

        elif password != repassword:
            errormessage['error'] = '비밀번호가 다릅니다'

            return render(request, 'signup.html', errormessage)

        else:
            # 데이터들을 넣어준다
            user = User(
                username=username,
                userid=userid,
                password=make_password(password),
                useremail=useremail,
                userimg=userimg
            )

            # 데이터 저장
            user.save()

        return redirect('/user/login/')

# 로그인


def login(request):
    # 로그인 시도할경우
    if request.method == 'POST':
        # 입력한 내용들을 받아오고
        form = LoginForm(request.POST)

        # 데이터가 있을경우
        if form.is_valid():
            # 세션에 pk값을 담아준다
            request.session['user'] = form.user_id

            return redirect('/home/')

    # 로그인 화면으로 가는경우
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


# 로그아웃
def logout(request):
    # 세션값이 있을경우(로그인 되어있는 경우)
    if request.session.get('user'):
        # 세션값을 지워준다
        del(request.session['user'])

    return redirect('/home/')
