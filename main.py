import pygame as pg

m, n, a = 40, 19, 10
w, h = 99*a, 43*a


def show(window, w, h, x, y, x1, y1, vec, k):
    while not((x == w and y == h) or (x == 0 and y == 0) or (x == w and y == 0) or (x == 0 and y == h)):

        if k:
            pg.draw.line(window, (0, 0, 0), (x1, y1), (x, y), 4)

        x1, y1, k = x, y, not k

        x, y = x + vec[0], y + vec[1]

        if x == 0 or int(x) == w:
            vec[0] = -vec[0]

        if y == 0 or int(y) == h:
            vec[1] = -vec[1]
    if k:
        pg.draw.line(window, (0, 0, 0), (x1, y1), (x, y), 3)


pg.init()
window = pg.display.set_mode((w, h), pg.RESIZABLE)
clock = pg.time.Clock()
window.fill((50, 150, 50))

simulation, edit, x, y, x1, y1, vec, k, W, H = True, True, a, a, 0, 0, [a, a], True, w, h
while simulation:
    if edit:
        show(window, w, h, x, y, x1, y1, vec, k)
        edit = False

    clock.tick(30)
    pg.display.flip()
    pg.display.set_caption('Цифровой бильярд ' + str(n) + ' x ' + str(m) + ', ' + str(a))

    for e in pg.event.get():
        if e.type == pg.QUIT:
            stop, simulation = False, False
        if e.type == pg.KEYUP and e.key == pg.K_UP:
            a += 1
        if e.type == pg.KEYUP and e.key == pg.K_DOWN and a > 1:
            a -= 1
        if pg.mouse.get_pressed()[0]:
            px, py = pg.mouse.get_pos()
            W, H = px + a + 50, py + a + 50
        if e.type == pg.VIDEORESIZE:
            W, H = e.w, e.h

        if e.type in [pg.KEYUP, pg.VIDEORESIZE] or pg.mouse.get_pressed()[0]:
            w, h = W - W % a, H - H % a
            window = pg.display.set_mode((w, h), pg.RESIZABLE)
            edit = True
            m, n = w // a, h // a
            x, y, x1, y1, vec, k = a, a, 0, 0, [a, a], True

            window.fill((50, 150, 50))
