from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.core.text import LabelBase
from kivy.lang import Builder

# 폰트 설정
LabelBase.register(name='Roboto', fn_regular='loginFont.ttf')

# Kivy Builder로 화면 레이아웃 정의
Builder.load_string('''
<LoginScreen>:
    orientation: 'vertical'
    padding: [50, 100, 50, 100]
    spacing: 10

    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: 30
        Label:
            text: '아이디'
            font_name: 'Roboto'
        TextInput:
            id: username_entry
            font_name: 'Roboto'
            font_size: 18
            multiline: False
            on_text_validate: root.validate_email()
            
    Label:
        id: warning_label
        text: 'asdf'
        height: 10
        font_name: 'Roboto'
        font_size: 14
        color: (1, 0, 0, 1)

    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: 30
        Label:
            text: '비밀번호'
            font_name: 'Roboto'
        TextInput:
            id: password_entry
            font_name: 'Roboto'
            font_size: 18
            multiline: False
            password: True

    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: 30
        CheckBox:
            id: save_id_checkbox
        Label:
            text: '아이디 저장'
            font_name: 'Roboto'

    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: None
        height: 30
        CheckBox:
            id: auto_login_checkbox
        Label:
            text: '자동 로그인'
            font_name: 'Roboto'

    Button:
        text: '로그인'
        font_name: 'Roboto'
        font_size: 18
        size_hint: 1, None
        height: 30
        on_release: root.login()

    
''')

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

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
