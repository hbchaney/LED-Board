# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 14:26:56 2022

@author: hbcha
"""

import pyglet 
from pyglet import shapes



window = pyglet.window.Window(768,768) 
batch =  pyglet.graphics.Batch()

def color_changer(c,frame): 
    

    
    
    window.clear() 
    circles = [] 
    r = 5
    spacing = 12
         
    
    for i in range(64): 
        for j in range(64): 
            circles.append(shapes.Circle(x=i*spacing+6,y=j*spacing+6,radius=r,color=(c,c,c),batch=batch))
    
    batch.draw()
    pyglet.image.get_buffer_manager().get_color_buffer().save(f'C:/Users/hbcha/Desktop/Pythoning/image_dump/frame{frame}.png')

    
        

@window.event
def on_draw(): 
    
    for x in range(5): 
        color_changer(x*10,x)
        
    window.close()
        
    
    
    


pyglet.app.run()
