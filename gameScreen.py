from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.properties import NumericProperty, ObjectProperty, ReferenceListProperty, StringProperty, Clock
from kivy.vector import Vector
import random
from kivy.animation import Animation
from kivy.core.window import Window


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)


class Block(Widget):
    pass


class RhythmGame(BoxLayout):
    score = NumericProperty(0)
    song = StringProperty("None")
    progress = NumericProperty(0)

    def __init__(self, **kwargs):
        super(RhythmGame, self).__init__(**kwargs)
        self.register_event_type('on_hit')
        Clock.schedule_interval(self.create_block, 2)

    def on_hit(self, button_num):
        self.score += 100
        print(f"Button {button_num} was hit!")

    def check_hit(self, button_num):
        self.dispatch('on_hit', button_num)

    def create_block(self, dt):
        # 랜덤으로 블록이 떨어지도록 설정
        random_button_num = random.randint(1, 4)

        block = Block()
        self.ids.block_layout.add_widget(block)

        # 블록이 버튼 위로 떨어지도록 설정
        button = self.ids["button_" + str(random_button_num)]
        x = button.x + button.width / 2 - block.width / 2
        y = button.y + button.height
        block.pos = (x, y)

        # 블록이 아래로 이동하도록 애니메이션 설정
        block_animation = Animation(y=0, duration=2)
        block_animation.start(block)

        # 블록이 떨어지는 동안에도 버튼을 누를 수 있도록 설정
        Clock.schedule_once(lambda dt: self.check_hit(random_button_num), 0.5)
