# Created by : David Wang
# Created on : 17 Oct 2017
# Created for : ICS3UR
# Daily Assignment - Unit3-06
# This program displays a walking man.

from __future__ import division
import ui
import time

walking_man_image = ui.Image.named('./assets/sprites/walk1.bmp')
walkingimageview = ui.ImageView(frame=(400, 40, 180, 180))
walkingimageview.image = walking_man_image

box = ['./assets/sprites/walk1.BMP', './assets/sprites/walk2.BMP', './assets/sprites/walk3.BMP', './assets/sprites/walk4.BMP', './assets/sprites/walk5.BMP', './assets/sprites/walk6.BMP', './assets/sprites/walk7.BMP', './assets/sprites/walk8.BMP', './assets/sprites/walk9.BMP', './assets/sprites/walk10.BMP']

@ui.in_background

def start_touch_up_inside(sender):
    
    count = 0
    
    while True:
        
        if count < 10:
            walking_man_image = ui.Image.named(box[count])
            walkingimageview.image = walking_man_image
            time.sleep(1/15)
            count = count + 1
        else:
            count = 0

view = ui.load_view()
view.add_subview(walkingimageview)
view.present('full_screen')
