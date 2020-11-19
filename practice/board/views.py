from django.shortcuts import render, redirect
from .models import Board
from user.models import User
from django.core.paginator import Paginator
from .forms import BoardForm
from django.http import Http404, HttpResponse


# Create your views here.

# 게시글 수정
def update(request, pk):
    board = Board.objects.get(pk=pk)

    detail = {}

    # 글을 수정하고 제출을 눌렀을 때
    if request.method == 'POST':

        form = BoardForm(request.POST)

        if form.is_valid():

            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']

            board.save()

            print('수정완료')

            return redirect('/board/detail/' + str(board.id))

    # 수정사항을 입력하기 위해 페이지에 처음 접속했을때(수정사항 입력창)
    else:
        form = BoardForm()

        detail['title'] = board.title
        detail['contents'] = board.contents
        detail['pk'] = board.id

        return render(request, 'update.html', detail)


# 게시글 삭제
def delete(request, pk):

    # 해당 게시글의 pk값을 찾은뒤
    board = Board.objects.get(pk=pk)

    # 해당 데이터 모두삭제
    board.delete()

    print('삭제완료')

    return redirect('/board/list/')


# 게시글 상세보기
def detail(request, pk):
    # 상세보기에 보여줄 값을 넣을 딕셔러니 선언
    detail = {}

    user_id = request.session.get('user')

    try:
        # 해당 게시글의 pk값을 가져온뒤
        board = Board.objects.get(pk=pk)

        user = User.objects.get(pk=user_id)

        # 해당 게시글의 데이터들을 선언한 딕셔러니에 넣어준다
        detail['pk'] = board.id
        detail['title'] = board.title
        detail['contents'] = board.contents
        detail['regdate'] = board.regdate
        detail['writer'] = board.writer

        print(board.writer)
        print(user.userid)
        if str(board.writer) == str(user.userid):
            print('true')
            detail['sign'] = 'true'

        else:
            print('false')
            detail['sign'] = 'false'

    # 해당게시글이 없을시에는 오류문구 출력
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')

    # 데이터들을 넣은 딕셔러니를 반환
    return render(request, 'detail.html', detail)


# 글쓰기
def write(request):

    # 글을 쓰고 제출을 눌렀을때
    if request.method == 'POST':

        # 폼에 입력된 데이터들을 가져온다.
        form = BoardForm(request.POST)

        if form.is_valid():

            # 세션값을 user_id에 저장
            user_id = request.session.get('user')

            # 해당 세션과 일치하는 유저의 데이터를 가져온다.
            user = User.objects.get(pk=user_id)

            # Board Model을 가져온다
            board = Board()

            # 모델에 form에 입력한 값을 넣어준다
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = user

            print('writer =' + str(user))

            # 넣어준 값을 저장
            board.save()
            print('success')

            return redirect('/board/list/')

    else:
        # 게시글을 쓰기위한 화면
        form = BoardForm()

    return render(request, 'write.html', {'form': form})


# 게시판 목록
def list(request):

    # Board에 저장돼있는 모든데이터를 id순서로 가져온다
    all_boards = Board.objects.all().order_by('id')
    # 페이징
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 5)

    boards = paginator.get_page(page)
    return render(request, 'list.html', {'boards': boards})
