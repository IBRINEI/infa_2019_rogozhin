from graph import windowSize, canvasSize
from graph import brushColor, penColor
from graph import polygon, circle, label
from math import sin, cos

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


def main_body(color, x_coord):
    penColor(color)
    brushColor(color)
    circle(x_coord, 769, 300)


def head(x_coord, r, g, b):
    brushColor(233, 200, 176)
    penColor(200, 200, 200)
    circle(x_coord, 384, 200)
    penColor(0, 0, 0)
    eyes(r, g, b, x_coord)
    nose_and_mouth(x_coord)
    hair(x_coord)


def eyes(color_red, color_green, color_blue, x_coord):
    brushColor(color_red, color_green, color_blue)
    penColor('black')
    circle(x_coord + 65, 349, 35)
    circle(x_coord - 65, 349, 35)
    brushColor('black')
    circle(x_coord + 65, 349, 10)
    circle(x_coord - 65, 349, 10)


def nose_and_mouth(x_coord):
    brushColor('brown')
    polygon([(x_coord + 20, 394), (x_coord - 20, 394), (x_coord, 424)])
    # Nose is above; mouth is below
    brushColor('red')
    polygon([(x_coord - 130, 454), (x_coord + 150, 454), (x_coord, 534)])


def left_arm(length, angle, x_coord):
    brushColor(233, 200, 176)
    penColor(200, 200, 200)
    polygon([(x_coord - 233, 569),
             (x_coord - 193, 549),
             (x_coord - 193 - length * cos(angle),
              549 + length * sin(angle),
             (x_coord - 233 - length * cos(angle),
              569 + length * sin(angle))])
    penColor('white')
    circle((2 * x_coord - length * cos(angle) - 233 - length * cos(angle) - 193)/2,
           (549 + length * sin(angle) + 569 + length * sin(angle))/2, 40)


def right_arm(length, angle, x_coord):
    brushColor(233, 200, 176)
    penColor(200, 200, 200)
    polygon([(x_coord + 167, 549), (x_coord + 207, 569),
             (x_coord + 207 + length * cos(angle),
              569 - length * sin(angle)),
             (x_coord + 167 + length * cos(angle),
              549 - length * sin(angle))])
    penColor('white')
    circle((2 * x_coord + length * cos(angle) + 207 + length * cos(angle) + 167)/2,
           (569 - length * sin(angle) + 549 - length * sin(angle))/2, 40)


# left guy start
main_body('orange', 463)

head(463)

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
main_body('green', 1263)

head(1263)

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
label('PYTHON is REALLY AMAZING!', 00, 00,
      font=('Arial 32', 90, 'bold'),
      bg='green',
      foreground='black')

run()
