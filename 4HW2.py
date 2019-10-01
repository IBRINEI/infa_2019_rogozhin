from graph import windowSize, canvasSize, run
from graph import brushColor, penColor
from graph import polygon, circle, label
from math import sin, cos


windowSize(3000, 1000)
canvasSize(1760, 769)


def hair(color, x_coord):
    brushColor(color)
    default_hair = [[(293 - 463 + x_coord, 275), (336 - 463 + x_coord, 219), (267 - 463 + x_coord, 205)],
                    [(316 - 463 + x_coord, 230), (378 - 463 + x_coord, 200), (329 - 463 + x_coord, 166)],
                    [(362 - 463 + x_coord, 201), (431 - 463 + x_coord, 186), (377 - 463 + x_coord, 149)],
                    [(417 - 463 + x_coord, 184), (476 - 463 + x_coord, 180), (436 - 463 + x_coord, 144)],
                    [(457 - 463 + x_coord, 187), (509 - 463 + x_coord, 186), (486 - 463 + x_coord, 143)],
                    [(498 - 463 + x_coord, 178), (543 - 463 + x_coord, 200), (525 - 463 + x_coord, 151)],
                    [(532 - 463 + x_coord, 187), (586 - 463 + x_coord, 220), (573 - 463 + x_coord, 152)],
                    [(576 - 463 + x_coord, 206), (621 - 463 + x_coord, 253), (615 - 463 + x_coord, 182)],
                    [(608 - 463 + x_coord, 235), (644 - 463 + x_coord, 289), (674 - 463 + x_coord, 218)]]
    for i in range(8):
        polygon(default_hair[i])


def main_body(color, x_coord):
    penColor(color)
    brushColor(color)
    circle(x_coord, 769, 300)
    penColor('black')
    brushColor(color)
    # shoulders
    polygon([(x_coord - 163, 629), (x_coord - 243, 629), (x_coord - 253, 539),
             (x_coord - 183, 489), (x_coord - 143, 549)])
    polygon([(x_coord + 237, 629), (x_coord + 157, 629), (x_coord + 147, 539),
             (x_coord + 217, 489), (x_coord + 257, 549)])


def head(x_coord, r, g, b, hair_color):
    brushColor(233, 200, 176)
    penColor(200, 200, 200)
    circle(x_coord, 384, 200)
    penColor(0, 0, 0)
    eyes(r, g, b, x_coord)
    nose_and_mouth(x_coord)
    hair(hair_color, x_coord)


def eyes(color_red, color_green, color_blue, x_coord):
    brushColor(color_red, color_green, color_blue)
    penColor('black')
    circle(x_coord + 65, 349, 35)
    circle(x_coord - 65, 349, 35)
    brushColor('black')
    circle(x_coord + 65, 349, 10)
    circle(x_coord - 65, 349, 10)


def nose_and_mouth(x_coord):
    # nose
    brushColor('brown')
    polygon([(x_coord + 20, 394), (x_coord - 20, 394), (x_coord, 424)])
    # mouth
    brushColor('red')
    polygon([(x_coord - 130, 454), (x_coord + 150, 454), (x_coord, 534)])


def left_arm(length, angle, x_coord):
    brushColor(233, 200, 176)
    penColor(200, 200, 200)
    polygon([(x_coord - 233, 569),
             (x_coord - 193, 549),
             (x_coord - 193 - length * cos(angle),
              549 + length * sin(angle)),
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


def guy(x_coord, body_color, hair_color, r, g, b, al, ll, ar, lr):
    # x_coord - x coordinate of the body circle center
    # r, g, b - eye color
    # ll, lr - lenght of left/right arm
    # al, ar - angle of left/right arm in radians
    left_arm(ll, al, x_coord)
    right_arm(lr, ar, x_coord)
    main_body(body_color, x_coord)
    head(x_coord, r, g, b, hair_color)


guy(463, 'orange', 'purple', 100, 100, 255, 4.936, 409, 1.106, 469)
guy(1263, 'green', 'yellow', 191, 200, 183, 4.936, 409, 1.106, 469)


# label on top; may not work with old OS/PC
label('PYTHON is REALLY AMAZING!', 00, 00,
      font=('Arial 32', 90, 'bold'),
      bg='green',
      foreground='black')

run()
