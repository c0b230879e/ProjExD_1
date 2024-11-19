import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))
FPS = 200

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    tmr = 0
    koukaton = pg.image.load("fig/3.png")
    koukaton = pg.transform.flip(koukaton,True,False)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        # for i in range(0,800):
        #     screen.blit(koukaton,[i,200])
        #     pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()