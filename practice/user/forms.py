from django import forms
from .models import User
from django.contrib.auth.hashers import check_password


# 로그인 화면 Form
class LoginForm(forms.Form):
    userid = forms.CharField(
        error_messages={
            'required': '아이디를 입력하세요.'
        },
        max_length=32, label='사용자아이디'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호')

    def clean(self):
        cleaned_data = super().clean()
        userid = cleaned_data.get('userid')
        password = cleaned_data.get('password')

        if userid and password:
            try:
                # userid에 입력한 값과 일치하는 데이터를 넣어준다.
                user = User.objects.get(userid=userid)
                print(user.username)
                print('user.id =' + str(user.id))
            except user.DoesNotExist:
                self.add_error('userid', '아이디가 없습니다.')
                return
            if not check_password(password, user.password):
                self.add_error('password', '비밀번호를 틀렸습니다.')
            # 유효성 검사에 문제가 없을경우
            else:
                # form.user_id 에 user.id 저장
                self.user_id = user.id
