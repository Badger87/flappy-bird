def on_button_pressed_a():
    birdie.turn(Direction.RIGHT, 90)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    birdie.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

birdie: game.LedSprite = None
birdie = game.create_sprite(0, 5)