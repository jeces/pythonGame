from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, db
import requests

from kivy.app import App
from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.core.text import LabelBase
from kivy.lang import Builder

# Firebase 초기화
cred = credentials.Certificate('pythongame-7e176-firebase-adminsdk-5yzva-dc941ab7c1.json')  # Firebase 서비스 계정 키 파일
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pythongame-7e176-default-rtdb.firebaseio.com'  # Firebase 실시간 데이터베이스 URL
})

# 폰트 설정
LabelBase.register(name='Roboto', fn_regular='loginFont.ttf')

# Kivy Builder로 화면 레이아웃 정의
Builder.load_file('signUpIn.kv')

# Flask 앱 초기화
app = Flask(__name__)

# Flask 라우트 및 핸들러
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    save_id = request.form.get('save_id')
    auto_login = request.form.get('auto_login')

    # 로그인 기능 구현
    # ...

    # 예시: Firebase에 로그인 정보 저장
    db.reference('users').push({
        'email': email,
        'password': password,
        'save_id': save_id,
        'auto_login': auto_login
    })

    return jsonify({'message': 'Logged in successfully'})

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')
    dob = request.form.get('dob')

    # Perform signup validation logic here
    # ...

    # 예시: Firebase에 회원가입 정보 저장
    db.reference('users').push({
        'email': email,
        'password': password,
        'name': name,
        'dob': dob
    })

    return jsonify({'message': 'Signed up successfully'})

# 클라이언트와의 연결을 위한 Flask 서버 실행
if __name__ == '__main__':
    app.run()

# Kivy 앱 클래스
class LoginScreen(BoxLayout):
    def validate_email(self):
        email = self.ids.email_entry.text
        if email and '@' not in email:
            self.ids.warning_label.text = 'Please enter a valid email'
        else:
            self.ids.warning_label.text = ''

    def login(self):
        email = self.ids.email_entry.text
        password = self.ids.password_entry.text
        save_id = self.ids.save_id_checkbox.active
        auto_login = self.ids.auto_login_checkbox.active

        # 서버로 로그인 요청을 보냄
        url = 'http://localhost:5000/login'  # Flask 서버의 URL
        data = {
            'email': email,
            'password': password,
            'save_id': save_id,
            'auto_login': auto_login
        }
        response = requests.post(url, data=data)

        if response.status_code == 200:
            print('Logged in successfully')
        else:
            print('Login failed')

    def open_signup_modal(self):
        modal_view = SignUpModal()
        modal_view.open()

    # 나머지 코드 생략

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

# Kivy 앱 실행
class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()