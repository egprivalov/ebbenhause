import pygame as pg
from math import cos, sin, pi
import pyautogui as pag

def snap_it(file_name:str) -> None:
    mypic = pag.screenshot(region=(500, 250, 900, 600))
    mypic.save(r"C:\Users\egodka\PyCharmProjects\Programs\eben_pics\{}".format(file_name))
    pass


class AroundCircle1:
    def __init__(self, width=40.0, height=40.0, x=0.0, y=0.0):
        self.width = width
        self.height = height
        self.centr = (x, y)
        self.is_incr = True

    def update(self):
        # if self.width >= 78:
        #     self.is_incr = False
        # elif self.width <= 40:
        #     self.is_incr = True

        if self.width >= 40:
            self.is_incr = False
        elif self.width <= 1:
            self.is_incr = True

        if self.is_incr:
            self.width += 1
            self.height -= 1
        else:
            self.width -= 1
            self.height += 1


class AroundCircle2:
    def __init__(self, width=110.0, height=110.0, x=0.0, y=0.0):
        self.width = width
        self.height = height
        self.centr = (x, y)
        self.is_incr = True

    def update(self):
        # if self.width >= 217:
        #     self.is_incr = False
        # elif self.width <= 110:
        #     self.is_incr = True

        if self.width >= 110:
            self.is_incr = False
        elif self.width <= 1:
            self.is_incr = True

        if self.is_incr:
            self.width += 2.75
            self.height -= 2.75
        else:
            self.width -= 2.75
            self.height += 2.75


class App:
    def __init__(self):
        self.FPS = 15
        self.clock = pg.time.Clock()
        pg.display.set_caption("eben")
        pg.display.set_icon(pg.image.load("imgs/bold_silver.png"))
        self.screen = pg.display.set_mode((1000, 800))
        self.centr_centr = (250, 400)
        self.centr_radius = 10
        self.colors = {"White": (255, 255, 255),
                       "Red": (255, 0, 0),
                       "Green": (0, 200, 0),
                       "Black": (0, 0, 0)}

    def run(self):
        pg.init()
        running = True

        around_circles1 = [AroundCircle1(x=self.centr_centr[0] + 90 * cos(pi/4*(i+1)+pi/8),
                                         y=self.centr_centr[1] + 90 * sin(pi/4*(i+1)+pi/8)) for i in range(8)]
        # around_circles2 = [AroundCircle2(x=1000 - self.centr_centr[0] -50 + 150 * cos(pi/3*(i+1)+pi/6),
        #                                  y=self.centr_centr[0] + 150 + 150 * sin(pi/3*(i+1)+pi/6)) for i in range(6)]
        around_circles2 = [AroundCircle2(x=1000 - self.centr_centr[0] - 50 + 150 * cos(pi / 3 * (i + 1)),
                                        y=self.centr_centr[0] + 150 + 150 * sin(pi / 3 * (i + 1))) for i in range(6)]
        switcher = False

        while running:
            self.clock.tick(self.FPS)
            self.screen.fill(self.colors["White"])
            pg.draw.circle(self.screen, self.colors["Red"], self.centr_centr, 50)
            pg.draw.circle(self.screen, self.colors["Red"], (1000 - self.centr_centr[0] - 50, self.centr_centr[1]), 50)
            for i in around_circles1:
                pg.draw.ellipse(self.screen, self.colors["Black"],
                                (i.centr[0]-i.width/2, i.centr[1]-i.height/2, i.width, i.height))
                if switcher:
                    i.update()
            for i in around_circles2:
                pg.draw.ellipse(self.screen, self.colors["Black"],
                                (i.centr[0] - i.width / 2, i.centr[1] - i.height / 2, i.width, i.height))
                if switcher:
                    i.update()

            # if around_circles2[0].height == around_circles2[0].width:
            #     switcher = False
            #     snap_it("goriz1.1.png")
            #
            # if 1.49 <= around_circles2[0].width / around_circles2[0].height <= 1.51:
            #     #switcher = False
            #     snap_it("goriz1.15.png")
            #
            # if 1.9 <= around_circles2[0].width / around_circles2[0].height <= 2.1:
            #     #switcher = False
            #     snap_it("goriz1.2.png")
            #
            # if 2.4 <= around_circles2[0].width / around_circles2[0].height <= 2.6:
            #     #switcher = False
            #     snap_it("goriz1.25.png")
            #
            # if 2.7 <= around_circles2[0].width / around_circles2[0].height <= 3.2:
            #     #switcher = False
            #     snap_it("goriz1.3.png")
            #
            # if 3.3 <= around_circles2[0].width / around_circles2[0].height <= 3.6:
            #     #switcher = False
            #     snap_it("goriz1.35.png")
            #
            # if 3.8 <= around_circles2[0].width / around_circles2[0].height <= 4.1:
            #     #switcher = False
            #     snap_it("goriz1.4.png")

            if 5.3 <= around_circles2[0].height / around_circles2[0].width <= 5.7:
                #switcher = False
                snap_it("goriz1.55.png")

            # if 4.8 <= around_circles2[0].width / around_circles2[0].height <= 5.2:
            #     #switcher = False
            #     snap_it("goriz1.5.png")

            # if 1.9 <= around_circles2[0].height / around_circles2[0].width <= 2.05:
            #     #switcher = False
            #     snap_it("1.2.png")
            #
            # if 1.4 <= around_circles2[0].height / around_circles2[0].width <= 1.6:
            #     #switcher = False
            #     snap_it("1.15.png")
            #
            # if 2.4 <= around_circles2[0].height / around_circles2[0].width <= 2.6:
            #     #switcher = False
            #     snap_it("1.25.png")
            #
            # if 3.4 <= around_circles2[0].height / around_circles2[0].width <= 3.6:
            #    # switcher = False
            #     snap_it("1.35.png")
            #
            # if 4.3 <= around_circles2[0].height / around_circles2[0].width <= 4.7:
            #     #switcher = False
            #     snap_it("1.45.png")
            #
            # if 2.999 <= around_circles2[0].height / around_circles2[0].width <= 3.001:
            #     #switcher = False
            #     snap_it("1.3.png")
            #
            # if 3.999 <= around_circles2[0].height / around_circles2[0].width <= 4.001:
            #     #switcher = False
            #     snap_it("1.4.png")
            #
            # if 4.9 <= around_circles2[0].height / around_circles2[0].width <= 5.2:
            #     #switcher = False
            #     snap_it("1.5.png")
            #

            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        if switcher:
                            switcher = False
                        else:
                            switcher = True


if __name__ == "__main__":
    App().run()
