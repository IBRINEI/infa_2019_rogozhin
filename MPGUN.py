from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = -10
        self.y = -10
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30
        self.xtbound = []
        self.ytbound = []
        for i in range(len(gr1.coords)):
            if self.x < gr1.coords[i][0]:
                self.xtbound.append(True)
            else:
                self.xtbound.append(False)
            if self.y < gr1.coords[i][1]:
                self.ytbound.append(True)
            else:
                self.ytbound.append(False)

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        if self.live <= 0:
            canv.delete(self.id)
        else:
            self.vy += 9.81 / 10
            self.x += self.vx
            self.y += self.vy
            self.set_coords()
            for i in range(1, len(gr1.coords)):
                c1 = (gr1.coords[i][0] - gr1.coords[i - 1][1])
                if c1 == 0:
                    c1 = 0.000001
                k = (gr1.coords[i][1] - gr1.coords[i - 1][1]) / c1
                if k == 0:
                    k = 0.0001
                k1 = - 1 / k
                c = gr1.coords[i - 1][1] - gr1.coords[i][1]
                d = gr1.coords[i][0] - gr1.coords[i - 1][0]
                e = gr1.coords[i - 1][0] * gr1.coords[i][1] - gr1.coords[i][0] * gr1.coords[i - 1][1]
                if ((abs(c * self.x + d * self.y + e) / math.sqrt(c * c + d * d)) < self.r) and (
                        c * (self.y - gr1.coords[i - 1][1]) - d * (self.x - gr1.coords[i - 1][0])) * (
                        c * (self.y - gr1.coords[i][1]) - d * (self.x - gr1.coords[i][0])) < 0:
                    self.x -= 2 * self.vx
                    self.y -= 2 * self.vy
                    self.exvx = self.vx
                    self.exvy = self.vy
                    self.vx = self.exvx - 2 * c * (self.exvx * c + self.exvy * d) / (c * c + d * d) * 0.5
                    self.vy = self.exvy - 2 * d * (self.exvx * c + self.exvy * d) / (c * c + d * d) * 0.5
                    self.x += 2 * self.vx
                    self.y += 2 * self.vy
                    self.set_coords()

    #        if self.x > self.xbound:
    #            self.x -= self.vx
    #            self.vx = -self.vx/2.5
    #        if self.y > self.ybound:
    #            self.y -= self.vy
    #            self.vy = -self.vy/2.5
    #            self.vx -= self.vx*0.15

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) < (self.r + obj.r):
            canv.delete(obj.id)
            obj.live = 0
            return True
        else:
            return False


class gun():
    def idle(self, event):
        pass

    def fire2_set(self, x, y):
        self.x = x + 15  # 20, 50
        self.y = y - 15  # 450, 420
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(self.x - 15, self.y + 15, self.x + 15, self.y - 15, width=7, fill='black')
        self.live = 1
        self.r = 15

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet, launched
        self.bullet += 1
        new_ball = ball()
        new_ball.r += 5
        new_ball.x = self.x - 15
        new_ball.y = self.y + 15
        self.an = math.atan((event.y - new_ball.y - 15) / (event.x - new_ball.x + 15))
        if self.an > 0 and event.x - new_ball.x + 15 < 0:
            new_ball.vx = -self.f2_power * math.cos(self.an)
            new_ball.vy = -self.f2_power * math.sin(self.an)
        else:
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = self.f2_power * math.sin(self.an)
        self.balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        launched = True
        self.launched = True

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - self.y + 15) / (event.x - self.x - 15))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        if (event.y - self.y + 15) / (event.x - self.x - 15) >= 0:
            canv.coords(self.id, self.x - 15, self.y + 15,
                        self.x - 15 - max(self.f2_power, 20) * math.cos(self.an),
                        self.y + 15 - max(self.f2_power, 20) * math.sin(self.an)
                        )
        else:
            canv.coords(self.id, self.x - 15, self.y + 15,
                        self.x - 15 + max(self.f2_power, 20) * math.cos(self.an),
                        self.y + 15 + max(self.f2_power, 20) * math.sin(self.an)
                        )
        # canv.coords(self.id)

    # self.an = math.atan((event.y - self.y) / (event.x - self.x))
    # if self.f2_on:
    #   canv.itemconfig(self.id, fill = 'orannge')
    # else:
    #    canv.itemconfig(self.id, fill = 'black')
    # canv.coords(self.id, self.x + 15, self.y - 15, )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class ground():
    def ground_set(self):
        self.on = False
        self.finish = False
        self.coords = []
        self.id = []
        self.end = True

    def draw_start(self, event):
        self.on = True

    def draw_finish(self, event):
        self.on = False
        self.finish = True
        self.really_draw()

    def draw(self, event):
        if self.on is True:
            self.coords.append((event.x, event.y))
        else:
            self.finish = True

    def really_draw(self):
        print(len(self.coords))
        for i in range(1, len(self.coords)):
            self.id.append(
                canv.create_line(self.coords[i - 1][0], self.coords[i - 1][1], self.coords[i][0], self.coords[i][1],
                                 width=3))
        self.end = False
        new_game()


gr1 = ground()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
g2 = gun()
g1.bullet = 0
g2.bullet = 0
g1.balls = []
g2.balls = []
g1.scoreq = 0
g1.scoreid = canv.create_text(100, 20, text='1: ' + str(g1.scoreq))
g2.scoreq = 0
g2.scoreid = canv.create_text(200, 10, text='2: ' + str(g2.scoreq))
g1.live = 1
g2.live = 1
g1.launched = False
g2.launched = True


def ground_draw():
    global gr1
    gr1.ground_set()
    canv.bind('<Button-1>', gr1.draw_start)
    canv.bind('<ButtonRelease-1>', gr1.draw_finish)
    canv.bind('<Motion>', gr1.draw)


def new_game(event=''):
    global gun, t1, screen1, balls, bullet, g1, b, t2, gr1, g2
    canv.itemconfig(screen1, text='')
    last = 1
    g1.fire2_set(20, 450)
    g2.fire2_set(620, 450)
    while g1.live and g2.live:
        canv.itemconfig(g1.scoreid, text='1: ' + str(g1.scoreq))
        canv.itemconfig(g2.scoreid, text='2: ' + str(g2.scoreq))
        if g2.launched is True and g1.launched is False:
            last = 1
            canv.bind('<Button-1>', g1.fire2_start)
            canv.bind('<ButtonRelease-1>', g1.fire2_end)
            canv.bind('<Motion>', g1.targetting)
            g1.power_up()
            for b in g1.balls:
                b.move()
                b.hittest(g2)
            if not g1.live or not g2.live:
                canv.bind('<Button-1>', g1.idle)
                canv.bind('<ButtonRelease-1>', g1.idle)
                canv.bind('<Motion>', g1.idle)
                if not g1.live:
                    canv.itemconfig(screen1, text='Игрок 2 победил за ' + str(g2.bullet) + ' выстрелов')
                    g2.scoreq += 0.5
                elif not g2.live:
                    canv.itemconfig(screen1, text='Игрок 1 победил за ' + str(g1.bullet) + ' выстрелов')
                    g1.scoreq += 0.5
                g1.live = 0
                canv.delete(g1.id)
                g2.live = 0
                canv.delete(g2.id)
            for b in g2.balls:
                b.move()
                b.hittest(g1)
            if (not g1.live or not g2.live) and not (g1.live == 0 and g2.live == 0):
                canv.bind('<Button-1>', g2.idle)
                canv.bind('<ButtonRelease-1>', g2.idle)
                canv.bind('<Motion>', g2.idle)
                if not g1.live:
                    canv.itemconfig(screen1, text='Игрок 2 победил за ' + str(g2.bullet) + ' выстрелов')
                    g2.scoreq += 0.5
                elif not g2.live:
                    canv.itemconfig(screen1, text='Игрок 1 победил за ' + str(g1.bullet) + ' выстрелов')
                    g1.scoreq += 0.5
                g1.live = 0
                canv.delete(g1.id)
                g2.live = 0
                canv.delete(g2.id)
            if g1.launched is True:
                print('2')
                g2.launched = False

        if g1.launched is True and g2.launched is False:
            last = 2
            canv.bind('<Button-1>', g2.fire2_start)
            canv.bind('<ButtonRelease-1>', g2.fire2_end)
            canv.bind('<Motion>', g2.targetting)
            g2.power_up()
            for b in g1.balls:
                b.move()
                b.hittest(g2)
            if not g1.live or not g2.live:
                canv.bind('<Button-1>', g1.idle)
                canv.bind('<ButtonRelease-1>', g1.idle)
                canv.bind('<Motion>', g1.idle)
                if not g1.live:
                    canv.itemconfig(screen1, text='Игрок 2 победил за ' + str(g2.bullet) + ' выстрелов')
                    g2.scoreq += 0.5
                elif not g2.live:
                    canv.itemconfig(screen1, text='Игрок 1 победил за ' + str(g2.bullet) + ' выстрелов')
                    g1.scoreq += 0.5
                g1.live = 0
                canv.delete(g1.id)
                g2.live = 0
                canv.delete(g2.id)
            for b in g2.balls:
                b.move()
                b.hittest(g1)
            if not g1.live or not g2.live:
                canv.bind('<Button-1>', g2.idle)
                canv.bind('<ButtonRelease-1>', g2.idle)
                canv.bind('<Motion>', g2.idle)
                if not g1.live:
                    canv.itemconfig(screen1, text='Игрок 2 победил за ' + str(g2.bullet) + ' выстрелов')
                    g1.scoreq += 0.5
                elif not g2.live:
                    canv.itemconfig(screen1, text='Игрок 1 победил за ' + str(g2.bullet) + ' выстрелов')
                    g2.scoreq += 0.5
                g1.live = 0
                canv.delete(g1.id)
                g2.live = 0
                canv.delete(g2.id)
            if g2.launched is True:
                g1.launched = False
        if g1.launched is True and g2.launched is True:
            if last == 1:
                g2.launched = False
            elif last == 2:
                g1.launched = False
        canv.update()
        time.sleep(0.03)

    canv.delete(g1.id)
    for i in g1.balls:
        canv.delete(i.id)
        g1.balls.remove(i)
    for i in g2.balls:
        canv.delete(i.id)
        g2.balls.remove(i)
    g1.bullet = 0
    g2.bullet = 0
    root.after(1000, new_game)


ground_draw()

canv.mainloop()
