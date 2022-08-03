#functions 8===D
#---------------------------
#position
#moveTo(x, y, duration = n)
#moveRel(x, y, duration = n)
#dragTo
#dragRel
#click(x, y)
#scroll(n<201)
#press('x')
#hotkey("x", "y")
#---------------------------

#important cursor locations
#---------------------------
# my cars 957, 518
# porsche after full scroll 694, 699
# right scroll autoshow 1822, 556
# cayman below gt3rs 1257, 695
# top of scroll bar manufacturer 1649, 262
# get in car 960, 454
# upgrades/tuning 512, 371
# car mastery 1589, 645
# remove car 952, 683
#---------------------------
import time
import pyautogui as pg

a=0

while a < 2:
#move to my cars, focus on game and press enter
    time.sleep(3)
    pg.moveTo(957, 518, duration = .5)
    pg.click(957, 518)
    pg.press('enter')

#pause for lag
    time.sleep(1)

#open manufacturers
    pg.press('backspace')

#pause for lag
    time.sleep(.5)

#scroll to bottom
    pg.moveTo(1649, 262, duration = .5)
    pg.dragRel(0, 250, duration = .5)

#select porsche
    pg.moveTo(694, 699, duration = .5)
    pg.press('enter')

#lag
    time.sleep(.5)

#scroll right
    pg.press('right', presses = 7, interval = .5)

#select cayman
    pg.moveTo(557, 731, duration = .5)
    pg.press('down')
    pg.press('enter')

#get in car
    pg.moveTo(960, 454, duration = .5)
    pg.press('enter')

#new car screen lag
    time.sleep(9)
    pg.press('escape')

#upgrades/tuning
    pg.click(512, 371, clicks = 2, duration = 1)
    pg.press('enter')

#lag
    time.sleep(1)

#car mastery
    pg.moveTo(1589, 645, duration = .5)
    pg.press('enter')

#lag
    time.sleep(.5)

#select skills
    pg.click(380, 627, clicks = 1, duration = 1.5)
    pg.press('enter')
    time.sleep(.5)
    pg.click(494, 634, clicks = 2, duration = .5)
    pg.press('enter')
    time.sleep(.5)
    pg.click(604, 632, clicks = 2, duration = .5)
    pg.press('enter')
    time.sleep(.5)
    pg.click(610, 505, clicks = 2, duration = .5)
    pg.press('enter')
    time.sleep(.5)
    pg.click(604, 392, clicks = 2, duration = .5)
    pg.press('enter')
    time.sleep(.5)
    pg.click(708, 499, clicks = 2, duration = .5)
    pg.press('enter')

#exit car mastery
    pg.press('escape', presses = 1)
    time.sleep(1)
    pg.press('escape', presses = 1)
    a = a + 1
#---------------------

while 3 > a > 1:
#move to my cars, focus on game and press enter
    time.sleep(3)
    pg.moveTo(957, 518, duration = .5)
    pg.click(957, 518)
    pg.press('enter')

#pause for lag
    time.sleep(1)

#open manufacturers
    pg.press('backspace')

#pause for lag
    time.sleep(.5)

#scroll to bottom
    pg.moveTo(1649, 262, duration = .5)
    pg.dragRel(0, 250, duration = .5)

#select porsche
    pg.moveTo(694, 699, duration = .5)
    pg.press('enter')

#lag
    time.sleep(.5)

#scroll right
    pg.press('right', presses = 7, interval = .5)

#select cayman
    pg.moveTo(557, 731, duration = .5)
    pg.press('down')
    pg.press('enter')
    time.sleep(1)

# remove car
    pg.moveTo(952, 683, duration = .5)
    pg.press('enter')
    time.sleep(1)

#select cayman
    pg.moveTo(557, 731, duration = .5)
    pg.press('down')
    pg.press('enter')
    time.sleep(1)

#get in car
    pg.moveTo(960, 454, duration = .5)
    pg.press('enter')

#new car screen lag
    time.sleep(9)
    pg.press('escape')

#upgrades/tuning
    pg.click(512, 371, clicks = 2, duration = 1)
    pg.press('enter')

#lag
    time.sleep(1)

#car mastery
    pg.moveTo(1589, 645, duration = .5)
    pg.press('enter')

#lag
    time.sleep(.5)

#select skills
    pg.click(380, 627, clicks = 1, duration = 1.5)
    pg.press('enter')
    time.sleep(.5)
    pg.click(494, 634, clicks = 2, duration = .5)
    pg.press('enter')
    time.sleep(.5)
    pg.click(604, 632, clicks = 2, duration = .5)
    pg.press('enter')
    time.sleep(.5)
    pg.click(610, 505, clicks = 2, duration = .5)
    pg.press('enter')
    time.sleep(.5)
    pg.click(604, 392, clicks = 2, duration = .5)
    pg.press('enter')
    time.sleep(.5)
    pg.click(708, 499, clicks = 2, duration = .5)
    pg.press('enter')

#exit car mastery
    pg.press('escape', presses = 2, interval = 1)
    a = a + 1