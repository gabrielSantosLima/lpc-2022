import turtle

def main():

  screen = turtle.Screen()
  screen.title('Meu Jogo')
  screen.bgcolor('black')
  screen.setup(width=800, height=660)
  screen.tracer(0)

  painter = turtle.Turtle()
  painter.speed(0)
  painter.shape('square')
  painter.color('white')
  painter.shapesize(stretch_wid=5, stretch_len=1)
  painter.up()
  painter.goto(-350, 0)

  painter_2 = turtle.Turtle()
  painter_2.speed(0)
  painter_2.shape('square')
  painter_2.color('white')
  painter_2.shapesize(stretch_wid=5, stretch_len=1)
  painter_2.up()
  painter_2.goto(350, 0)
  
  ball = turtle.Turtle()
  ball.speed(0)
  ball.shape('square')
  ball.color('white')
  ball.penup()
  ball.goto(0, 0)
  ball.dx = 1
  ball.dy = 1

  hud = turtle.Turtle()
  hud.speed(0)
  hud.shape('square')
  hud.color('white')
  hud.hideturtle()
  hud.penup()
  hud.goto(0, 260)
  hud.write("0 : 0", align="center", font=("Roboto", 24, "normal"))

  while True:
    screen.update()

main()