import turtle
import random
import time

# Skor tablosu nesnesi oluşturuyoruz.
skor_tablosu = turtle.Turtle()

# Skor tablosunu çiziyoruz.
skor_tablosu.penup()
skor_tablosu.goto(-50, 240)
skor_tablosu.write("Skor: 0", font=("Arial", 20, "normal"))

# Kaplumbağa nesnesi oluşturuyoruz.
kaplumbaga = turtle.Turtle()
kaplumbaga.penup()

# Hareket fonksiyonu
# Hareket fonksiyonu
def move():
    global skor
    x = kaplumbaga.xcor() + random.randint(-200, 200)
    y = kaplumbaga.ycor() + random.randint(-200, 200)
    if abs(x) > 200:
        x = kaplumbaga.xcor()
    if abs(y) > 200:
        y = kaplumbaga.ycor()
    kaplumbaga.setpos(x, y)
    global skor
    skor += 1
    skor_tablosu.clear()
    print("Score:", skor)
    skor_tablosu.write("Skor: {}".format(skor), font=("Arial", 20, "normal"))

# Ana program
skor = 0
turtle.onscreenclick(move)
kaplumbaga.speed(5)
while True:
    move()
    time.sleep(0.8)
turtle.mainloop()




