from graph import *
from math import *

windowSize(1760, 769)
canvasSize(1760, 769)


def hair(color, shift_from_left_guy):
    brushColor(color)
    a = shift_from_left_guy
    polygon([(293 + a, 275), (336 + a, 219), (267 + a, 205)])
    polygon([(316 + a, 230), (378 + a, 200), (329 + a, 166)])
    polygon([(362 + a, 201), (431 + a, 186), (377 + a, 149)])
    polygon([(417 + a, 184), (476 + a, 180), (436 + a, 144)])
    polygon([(457 + a, 187), (509 + a, 186), (486 + a, 143)])
    polygon([(498 + a, 178), (543 + a, 200), (525 + a, 151)])
    polygon([(532 + a, 187), (586 + a, 220), (573 + a, 152)])
    polygon([(576 + a, 206), (621 + a, 253), (615 + a, 182)])
    polygon([(608 + a, 235), (644 + a, 289), (674 + a, 218)])


def main_body(color, shift_from_left_guy):
    penColor(color)
    brushColor(color)
    circle(463 + shift_from_left_guy, 769, 300)


def head(shift_from_left_guy):
    a = shift_from_left_guy
    brushColor(233, 200, 176)
    penColor(200, 200, 200)
    circle(463 + a, 384, 200)
    penColor(0, 0, 0)


def eyes(color_red, color_green, color_blue, shift_from_left_guy):
    brushColor(color_red, color_green, color_blue)
    penColor('black')
    circle(528 + shift_from_left_guy, 349, 35)
    circle(398 + shift_from_left_guy, 349, 35)
    brushColor('black')
    circle(528 + shift_from_left_guy, 349, 10)
    circle(398 + shift_from_left_guy, 349, 10)


def nose_and_mouth(shift_from_left_guy):
    a = shift_from_left_guy
    brushColor('brown')
    polygon([(483 + a, 394), (443 + a, 394), (463 + a, 424)])
    # Nose is above; mouth is below
    brushColor('red')
    polygon([(333 + a, 454), (613 + a, 454), (463 + a, 534)])


def left_arm(length, angle, shift_from_left_guy):
    a = shift_from_left_guy
    brushColor(233, 200, 176)
    penColor(200, 200, 200)
    polygon([(230 + a, 569), (270 + a, 549), (270 - length * cos(angle) + a, 549 + length * sin (angle)), (230 - length * cos(angle) + a, 569 + length * sin(angle))])
    penColor('white')
    circle((270 - length * cos(angle) + a + 230 - length * cos(angle) + a)/2, (549 + length * sin (angle) + 569 + length * sin(angle))/2, 40)


def right_arm(length, angle, shift_from_left_guy):
    a = shift_from_left_guy
    brushColor(233, 200, 176)
    penColor(200, 200, 200) 
    polygon([(630 + a, 549), (670 + a, 569), (670 + length * cos(angle) + a, 569 - length * sin (angle)), (630 + length * cos(angle) + a, 549 - length * sin (angle))])
    penColor('white')
    circle((670 + length * cos(angle) + a + 630 + length * cos(angle) + a)/2, (569 - length * sin (angle) + 549 - length * sin (angle))/2, 40)


# left guy start
main_body('orange', 0)

head(0)

eyes(100, 100, 255, 0)

nose_and_mouth(0)

left_arm(409, 4.936, 0)

right_arm(469, 1.106, 0)




penColor('black')
brushColor('orange')
polygon([(300, 629), (220, 629), (210, 539), (280, 489), (320, 549)])
polygon([(700, 629), (620, 629), (610, 539), (680, 489), (720, 549)])

hair('purple', 0)
# left guy end

# second guy start
main_body('green', 800)

head(800)

eyes(191, 200, 183, 800)

nose_and_mouth(800)

left_arm(409, 4.936, 800)

right_arm(469, 1.106, 800)

penColor('black')
brushColor('green')
polygon([(1100, 629), (1020, 629), (1010, 539), (1080, 489), (1120, 549)])
polygon([(1500, 629), (1420, 629), (1410, 539), (1480, 489), (1520, 549)])

hair('yellow', 800)
# second guy end
brushColor('black')

# label on top; may not work with old OS/PC
label('PYTHON is REALLY AMAZING!', 00, 00, font=('Arial 32', 90, 'bold'), bg='green', foreground='black')

run()
