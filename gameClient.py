from kivy.app import App
from kivy.event import EventDispatcher
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.uix.modalview import ModalView
from kivy.core.text import LabelBase
from kivy.lang import Builder

# 폰트 설정
LabelBase.register(name='Roboto', fn_regular='loginFont.ttf')

# Kivy Builder로 화면 레이아웃 정의
Builder.load_file('signUpIn.kv')


class LoginScreen(BoxLayout):
    def validate_email(self):
        email = self.ids.username_entry.text
        if email and '@' not in email:
            self.ids.warning_label.text = 'Please enter a valid email'
        else:
            self.ids.warning_label.text = ''

    def login(self):
        # 로그인 기능 구현
        username = self.ids.username_entry.text
        password = self.ids.password_entry.text
        save_id = self.ids.save_id_checkbox.active
        auto_login = self.ids.auto_login_checkbox.active
        print(f'Username: {username}')
        print(f'Password: {password}')
        print(f'Save ID: {save_id}')
        print(f'Auto Login: {auto_login}')

    def open_signup_modal(self):
        modal_view = SignUpModal()
        modal_view.open()


class SignUpModal(ModalView):
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

    def show_confirmation(self, *args):
        confirmation_modal = ConfirmationModal()  # 확인창 객체 생성
        confirmation_modal.bind(on_yes=self.return_to_login, on_no=self.return_to_signup)  # 확인창이 닫힐 때 로그인 창으로 돌아가도록 바인딩
        confirmation_modal.open()  # 확인창 열기

    def return_to_login(self, instance):
        print("Returning to login...")
        self.dismiss()
        # 로그인 창으로 돌아가는 로직을 작성하세요
        # 예를 들어, 앱의 상태를 초기화하거나 다른 화면으로 전환하는 등의 작업을 수행할 수 있습니다.

    def return_to_signup(self, instance):
        print("Returning to signup...")
        self.dismiss()

    # 회원가입 창으로 돌아가는 로직을 작성하세요
        # 예를 들어, 입력된 정보를 초기화하거나 다른 화면으로 전환하는 등의 작업을 수행할 수 있습니다.


# 확인창 클래스
class ConfirmationModal(ModalView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def dispatch_yes(self, *args):
        self.dismiss()
        self.dispatch('on_yes')

    def dispatch_no(self, *args):
        self.dispatch('on_no')


class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
