from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=64, verbose_name='글제목')
    contents = models.TextField(verbose_name='글내용')
    writer = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='작성자')
    regdate = models.DateTimeField(auto_now_add=True, verbose_name='작성일')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'practice_board'
        verbose_name = '연습보드 게시판'
        verbose_name_plural = '연습보드 게시판'
