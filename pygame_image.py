import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    pg.fps = 200
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    tmr = 0
    koukaton = pg.image.load("fig/3.png")
    bg_img_gyaku = pg.image.load("fig/pg_bg.jpg")
    bg_img_gyaku = pg.transform.flip(bg_img_gyaku,True,False)
    koukaton = pg.transform.flip(koukaton,True,False)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_gyaku,[-x+1600,0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bg_img_gyaku,[-x+4800,0])
        screen.blit(koukaton,[300,200])
        
        pg.display.update()
        
        tmr += 1  
        # if tmr == 800:
        #     screen.blit(bg_img_gyaku, [-tmr, 0])
        #     tmr =0      
        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()