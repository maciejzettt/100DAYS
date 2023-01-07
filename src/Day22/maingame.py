from time import sleep
from paddle import PongPaddle
from net import PongNet
from ball import PongBall
from gamefieldcontainer import GameFieldContainer
from score import PongScore


game = GameFieldContainer(field_height=400, field_width=700, window_title='PONG')
game.register_component('Net', PongNet)
game.register_component('Paddle A', PongPaddle, player_binding='A')
game.register_component('Paddle B', PongPaddle, player_binding='B')
game.register_component('Score A', PongScore, player_binding='A', x_pos=-80)
game.register_component('Score B', PongScore, player_binding='B', x_pos=80)
game.register_component('Ball', PongBall)
game.components_init()
game.register_action('Paddle A', 'w', 'move_up')
game.register_action('Paddle B', 'Up', 'move_up')
game.register_action('Paddle A', 's', 'some')
game.register_action('Paddle B', 'Down', 'move_down')

while game.is_valid():
    game.step_through_components()
    sleep(0.02)
game.screen.exitonclick()


