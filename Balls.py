from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

width = 800
height = 600
cont = True

colors = ['red', 'orange', 'black', 'green', 'blue']
score = 0


# Makes a stationary ball, that is deleted on click
# Click - +1 point
# No click - -1 point
# Missed click  - -2 points
# Additional feature - function create_ball makes the ball shrink a little bit with time1
def new_ball():
    global x, y, r, cont, score, color_new, create_ball_cont, num
    if cont and overall_cont:
        for i in range(num):
            canv.delete('new_ball_' + str(i))

        def create_ball():
            global r, color_new, create_ball_cont
            if create_ball_cont is True:
                for j in range(num):
                    r[j] -= 0.1
                    canv.delete('new_ball_' + str(j))
                    canv.create_oval(x[j] - r[j], y[j] - r[j], x[j] + r[j], y[j] + r[j], fill=color_new[j], width=0,
                                     tag='new_ball_'+str(j))
                root.after(2, create_ball)
        score -= 1
        root.after(5, create_ball_cont_true)
        root.after(6, create_ball)
        root.after(500, new_ball)
        root.after(500, rnd_coord_new_ball)
        root.after(500, create_ball_cont_false)
    elif overall_cont:
        cont = True
    else:
        pass


def create_ball_cont_true():
    global create_ball_cont
    create_ball_cont = True


def create_ball_cont_false():
    global create_ball_cont
    create_ball_cont = False


def rnd_coord_new_ball():
    global x, y, r, color_new, num
    x = []
    y = []
    r = []
    color_new = []
    for i in range(num):
        x.append(rnd(100, 700))
        y.append(rnd(100, 500))
        r.append(rnd(30, 50))
        color_new.append(choice(colors))


# Makes a score label, refreshing every 500 ms
def score_label():
    global score
    canv.delete('score')
    canv.create_text(100, 10, text=('SCORE:', score), anchor=NW, tag='score', justify=CENTER, font=('Arial 32', 20))
    canv.after(500, score_label)


# Randomizes coordinates for exotic ball
def exotic_ball_coord():
    global xe, ye, xr1, yr1, rie, roe
    xe = rnd(200, 550)
    ye = rnd(250, 350)
    xr1 = xe
    yr1 = ye
    roe = rnd(50, 70)
    rie = rnd(5, 10)


# Randomizes direction of a ball
def moving_ball_dir():
    global x_dir, y_dir
    x_dir = rnd(19999)/10000
    if x_dir > 1:
        x_dir = 1 - x_dir
    y_dir = rnd(19999)/10000
    if y_dir > 1:
        y_dir = 1 - y_dir


def moving_ball_dir_1():
    global x_dir_1, y_dir_1
    x_dir_1 = rnd(19999)/10000
    if x_dir_1 > 1:
        x_dir_1 = 1 - x_dir_1
    y_dir_1 = rnd(19999)/10000
    if y_dir_1 > 1:
        y_dir_1 = 1 - y_dir_1


# Inside part of exotic ball, moves strangely and fast
def moving_ball_1():
    global xr1, yr1, x_dir_1, y_dir_1, xe, ye, roe, rie, exotic_ball_clickable
    if overall_cont and exotic_ball_cont:
        xr1 += x_dir_1 * 4
        yr1 += y_dir_1 * 4
        if (xr1 - rie < xe - roe) or (xr1 + rie > xe + roe) or (yr1 - rie < ye - roe) or (yr1 + rie > ye + roe):
            xr1 -= x_dir_1 * 4
            yr1 -= y_dir_1 * 4
            moving_ball_dir_1()
        if (xr1 - rie < xe - roe) or (xr1 + rie > xe + roe) or (yr1 - rie < ye - roe) or (yr1 + rie > ye + roe):
            exotic_ball_clickable = False
        else:
            exotic_ball_clickable = True
        canv.delete('m_ball1')
        canv.create_rectangle(xr1 - rie, yr1 - rie, xr1 + rie, yr1 + rie, fill='white', width=0, tag='m_ball1')
        canv.after(1, moving_ball_1)
    else:
        pass


# Exotic ball is a ball that spawns only once and consists of two parts
# Outside part is a ball that just moves (coords xe, ye, roe(as radius))
# Inside part is a square, moving fast inside the outside ball(coords xr1, xr2, rie(as radius))
# Click on the inside ball - +50 points
# After click it disappears forever
def exotic_ball():
    global xe, ye, roe, rie
    if exotic_ball_cont and overall_cont:
        xe += x_dir * 4
        ye += y_dir * 4
        if (xe - roe < 0) or (xe + roe > width) or (ye - roe < 0) or (ye + roe > height):
            xe -= x_dir * 8
            ye -= y_dir * 8
            moving_ball_dir()
        canv.delete('e_b_o')
        canv.create_oval(xe - roe, ye - roe, xe + roe, ye + roe, fill='blue', width=0, tag='e_b_o')
        root.after(10, exotic_ball)
    else:
        pass


overall_cont = True
exotic_ball_cont = True
exotic_ball_clickable = True
create_ball_cont = True


def click(event):
    global score, cont, exotic_ball_cont, num
    if overall_cont:
        for i in range(num):
            if (abs(event.x - x[i]) < r[i]) and (abs(event.y - y[i]) < r[i]):
                score += 2
                canv.delete('new_ball_' + str(i))
                cont = False
                new_ball()
            else:
                score -= 2
        if (abs(event.x - xr1) < rie) and (abs(event.y < yr1) < rie) and (exotic_ball_cont is True) and \
                (exotic_ball_clickable is True):
            score += 52
            exotic_ball_cont = False
            root.after(10, canv.delete('e_b_o', 'm_ball1'))
    else:
        pass


# imports a leaderboard from local file, adds current player with score after 60 seconds, sorts it
def leaderboard():
    global score, name
    d = {}
    file1 = 'text.txt'
    with open(file1) as file:
        for line in file:
            key, *value = line.split()
            d[key] = int(value[0])
    if not isinstance(d.get(name), int):
        d.update({name: score})
    elif score > d.get(name):
        d.update({name: score})
    my_file = open(file1, "w")
    d1 = sorted(d.items(), key=lambda item: (-item[1], item[0]))
    for i in range(len(d)):
        my_file.write(f"{d1[i][0]} {d1[i][1]}\n")
    my_file.close()


def deny():
    global overall_cont
    overall_cont = False


num = 10

print("Type your name:")
name = input()

score_label()
exotic_ball_coord()
moving_ball_dir()
moving_ball_dir_1()
rnd_coord_new_ball()
new_ball()
exotic_ball()
moving_ball_1()

root.after(60000, deny)

root.after(60500, leaderboard)


canv.bind('<Button-1>', click)
mainloop()
