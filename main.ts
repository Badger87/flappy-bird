input.onButtonPressed(Button.A, function () {
    birdie.turn(Direction.Right, 90)
})
input.onButtonPressed(Button.B, function () {
    birdie.move(1)
})
input.onGesture(Gesture.Shake, function () {
	
})
let birdie: game.LedSprite = null
birdie = game.createSprite(0, 5)
