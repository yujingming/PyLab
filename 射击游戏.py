import turtle
turtle.showturtle
turtle.setup(500,500)
RADIUS = 20
PROJECT_SPEED = 10
FORCE_FACTOR = 20
NORTH = 90
WEST = 180
SOUTH = 270
EAST = 0
TATGET_X = 100
TARGET_Y = 100
turtle.penup()
turtle.goto(TATGET_X,TARGET_Y-RADIUS)
turtle.pendown()
turtle.circle(RADIUS)
turtle.penup()
turtle.goto(0,0)
angle=float(input('输入射击角度：'))
force=float(input('输入射击力度：')) 
distance = force * FORCE_FACTOR
turtle.pendown()
turtle.setheading(angle)
turtle.forward(distance)
if ((turtle.xcor()-TATGET_X)**2+(turtle.ycor()-TARGET_Y)**2)**0.5<=RADIUS:
    print('恭喜！''成功命中目标')
else:
    if angle>=90:
        print('未能命中，''试着调低角度')
    else:
        if distance>=170:
            print('未能命中，''试着降低射击力度')
        else:
            distance<=100
            print('未命中，''试着加强射击力度')
            if angle==90 and distance<170 and distance>100:
                print('运气问题，''再来一次')
turtle.done()