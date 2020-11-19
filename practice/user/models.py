from django.db import models

# Create your models here.


# 모델생성
class User(models.Model):
    userid = models.CharField(max_length=32, verbose_name='아이디')
    username = models.CharField(max_length=32, verbose_name='이름')
    password = models.CharField(max_length=32, verbose_name='비밀번호')
    # useremail 추가
    useremail = models.EmailField(
        max_length=64, verbose_name='이메일', default='None')
    regdate = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    # userimg 추가
    userimg = models.ImageField(
        blank=True,  upload_to="images", verbose_name='유저이미지', default="None")

    # admin 페이지에서 문자열로 보이게 해줌

    def __str__(self):
        return self.userid

    # admin 사용 편리를 위해 meta 클래스 생성
    class Meta:
        db_table = 'practice_user'
        verbose_name = '연습보드 사용자'
        verbose_name_plural = '연습보드 사용자'
