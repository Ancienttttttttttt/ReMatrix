import turtle

window = turtle.Screen()#отрисовка окна
window.title("Turtle!")#заголовок
turtle.shape("turtle")#отрисовка черепашки

#рисование квадрата
m = 4
for i in range(m):
    turtle.forward(100)#смещение черепашки на 100 пикселей
    turtle.right(90)#черепашка поварачивается на 90 градусов


#рисование круга
turtle.penup()
turtle.back(50)
turtle.pendown()
turtle.circle(100)#радиус круга

#рисование треугольника
n = 3#переменная для сторон треугольника
angle = 60#черепашка поварачивается на 60 градусов
turtle.penup()
turtle.forward(300)
turtle.pendown()
for i in range(n):
    turtle.forward(100)
    turtle.left(180 - angle)#вычитаем из 180 угол поворота

#рисование 5-угольника
i = 5
angle1 = 60
turtle.penup()
turtle.right(180 - angle1)
turtle.forward(150)
turtle.pendown()
x = (i - 2) * 180 / i
for j in range(i):
    turtle.forward(100)
    turtle.left(180 - x)


window.exitonclick()#закрытие окна
