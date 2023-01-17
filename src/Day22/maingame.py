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
game.register_action('Paddle A', 's', 'move_down')
game.register_action('Paddle B', 'Down', 'move_down')

while game.is_valid():
    game.step_through_components()
    if game.get_component_instance_by_name('Paddle A').detect_ball_collision(game.get_component_instance_by_name('Ball')):
        print("Ball collision A")
        game.get_component_instance_by_name('Ball').bounce_paddle()
    if game.get_component_instance_by_name('Paddle B').detect_ball_collision(game.get_component_instance_by_name('Ball')):
        print("Ball collision B")
        game.get_component_instance_by_name('Ball').bounce_paddle()
    exited = game.get_component_instance_by_name('Ball').exited_field()
    if exited:
        print(f"Ball exited the field and scored for {exited}.")
        game.get_component_instance_by_name('Score ' + exited).increase_score(1)
        game.update_screen()
        game.reinitialize_component('Ball')
        sleep(1)

    sleep(0.01)
game.screen.exitonclick()


