import pyautogui as pg
import time
pg.click(4,2,5)
pg.click (1107, 33, 1)
pg.hotkey ('winleft', 'ctrl', 'd')
pg.hotkey('winleft')
pg.typewrite ('chrom\n' ,0.5)
pg.hotkey ('winleft', 'up')
pg.typewrite ('www.glossier.com\n' ,0.5)
pg.moveTo (178, 159, 3)
time.sleep (3)
pg.click (347, 430)
time.sleep (5)
pg.click (690, 168)


