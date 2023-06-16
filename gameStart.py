from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock


class Ball(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class BallGame(Widget):
    def __init__(self, **kwargs):
        super(BallGame, self).__init__(**kwargs)
        self.ball = Ball(center=self.center)
        self.add_widget(self.ball)
        self.ball.velocity = Vector(6, 0).rotate(45)

    def update(self, dt):
        self.ball.move()

        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1


class BallApp(App):
    def build(self):
        game = BallGame()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    BallApp().run()
