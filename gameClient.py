from kivy.app import App
from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.core.text import LabelBase
from kivy.lang import Builder
import requests

# 폰트 설정
LabelBase.register(name='Roboto', fn_regular='loginFont.ttf')

# Kivy Builder로 화면 레이아웃 정의
Builder.load_file('signUpIn.kv')


class LoginScreen(BoxLayout):
    SERVER_URL = 'http://127.0.0.1:5000'  # 실제 서버 주소와 포트로 변경해주세요

    def validate_email(self):
        email = self.ids.email_entry.text
        if email and '@' not in email:
            self.ids.warning_label.text = 'Please enter a valid email'
        else:
            self.ids.warning_label.text = ''

    def login(self):
        # 로그인 기능 구현
        email = self.ids.email_entry.text
        password = self.ids.password_entry.text
        save_id = self.ids.save_id_checkbox.active
        auto_login = self.ids.auto_login_checkbox.active
        print(f'Email: {email}')
        print(f'Password: {password}')
        print(f'Save ID: {save_id}')
        print(f'Auto Login: {auto_login}')

        # 서버로 로그인 요청을 보냄
        response = requests.post(f'{self.SERVER_URL}/login', data={
            'email': email,
            'password': password,
            'save_id': save_id,
            'auto_login': auto_login
        })

        if response.status_code == 200:
            print('Login success')
            # 로그인 성공 처리 로직 구현
            # ...
        else:
            print('Login failed')
            # 로그인 실패 처리 로직 구현
            # ...

    def open_signup_modal(self):
        modal_view = SignUpModal()
        modal_view.open()

    def on_textinput(self):
        if self.ids.email_entry.focus:
            instance_email = self.ids.email_entry
            if instance_email.text == "":
                email_text = instance_email
            else:
                email_text = instance_email.text[-1]
            email_full_text = instance_email.text
            if (email_text == '\t') & self.ids.email_entry.focus:
                self.ids.email_entry.text = email_full_text[:-1]
                self.ids.password_entry.focus = True
        elif self.ids.password_entry.focus:
            instance_password = self.ids.password_entry
            if instance_password.text == "":
                password_text = instance_password
            else:
                password_text = instance_password.text[-1]
            password_full_text = instance_password.text
            if (password_text == '\t') & self.ids.password_entry.focus:
                self.ids.password_entry.text = password_full_text[:-1]
                self.ids.email_entry.focus = True


class SignUpModal(ModalView, EventDispatcher):
    def validate_email(self, instance):
        email = self.ids.email_input.text
        password = self.ids.password_input.text
        confirm_password = self.ids.confirm_password_input.text
        name = self.ids.name_input.text
        dob = self.ids.dob_input.text

    def submit_signup(self):
        email = self.ids.email_input.text
        password = self.ids.password_confirm_input.text
        name = self.ids.name_input.text
        dob = self.ids.dob_input.text

        # Perform signup validation logic here
        # ...

        # 서버로 로그인 요청을 보냄
        response = requests.post(f'{self.SERVER_URL}/signup', data={
            'email': email,
            'password': password,
            'name': name,
            'dob': dob
        })

        if response.status_code == 200:
            print('SignUo success')
            # 로그인 성공 처리 로직 구현
            # ...
        else:
            print('SignUo failed')
            # 로그인 실패 처리 로직 구현
            # ...



    def show_confirmation(self, *args):
        confirmation_modal = ConfirmationModal()  # 확인창 객체 생성
        confirmation_modal.on_yes = self.return_to_login  # Yes 버튼 클릭 시 로그인 창으로 돌아가도록 설정
        confirmation_modal.on_no = self.return_to_signup  # No 버튼 클릭 시 회원가입 창으로 돌아가도록 설정
        confirmation_modal.open()  # 확인창 열기

    def return_to_login(self):
        print('Returning to login...')
        self.dismiss()
        # 로그인 창으로 돌아가는 로직을 작성하세요
        # 예를 들어, 앱의 상태를 초기화하거나 다른 화면으로 전환하는 등의 작업을 수행할 수 있습니다.

    def return_to_signup(self):
        print('Returning to signup...')
        # 회원가입 창으로 돌아가는 로직을 작성하세요
        # 예를 들어, 입력된 정보를 초기화하거나 다른 화면으로 전환하는 등의 작업을 수행할 수 있습니다.


# 확인창 클래스
class ConfirmationModal(ModalView):
    on_yes = ObjectProperty(None)
    on_no = ObjectProperty(None)

    def close_confirmation(self, confirmed):
        self.dismiss()
        if confirmed:
            print('Membership registration confirmed')
            if self.on_yes:
                self.on_yes()
        else:
            print('Membership registration cancelled')
            if self.on_no:
                self.on_no()


class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()