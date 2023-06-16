from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.core.window import Window

from gameScreen import GameScreen
from loginScreen import LoginScreen

# 폰트 설정
LabelBase.register(name='Roboto', fn_regular='loginFont.ttf')

# Kivy Builder로 화면 레이아웃 정의
Builder.load_file('signUpIn.kv')


class GameApp(App):
    def build(self):
        # 전체 화면 크기 설정
        Window.size = (800, 600)  # 원하는 크기로 변경
        # ScreenManager 생성
        screen_manager = ScreenManager()

        # 로그인 화면과 게임 화면 생성
        login_screen = LoginScreen(name='login')
        game_screen = GameScreen(name='game')

        # ScreenManager에 화면 추가
        screen_manager.add_widget(login_screen)
        screen_manager.add_widget(game_screen)

        return screen_manager


if __name__ == '__main__':
    GameApp().run()
