from kivy.app import App
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
            self.ids.warning_label.text = '유효한 이메일을 입력해주세요.'
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
        confirmation_modal.open()  # 확인창 열기

# 확인창 클래스
class ConfirmationModal(ModalView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.6, 0.4)

        confirmation_layout = BoxLayout(orientation="vertical", padding=40, spacing=20)
        confirmation_label = Label(text="Are you sure you want to complete membership registration?", font_size=20, bold=True)
        confirmation_layout_button = BoxLayout(orientation="horizontal", padding=20, spacing=20)

        yes_button = Button(text="Yes", on_release=self.dismiss)
        no_button = Button(text="No", on_release=self.dismiss)

        confirmation_layout_button.add_widget(yes_button)
        confirmation_layout_button.add_widget(no_button)

        confirmation_layout.add_widget(confirmation_label)
        confirmation_layout.add_widget(confirmation_layout_button)

        self.add_widget(confirmation_layout)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()