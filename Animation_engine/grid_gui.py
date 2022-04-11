# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 14:26:56 2022

@author: hbcha
"""

import pyglet 
from pyglet import shapes
import os 

filename = "rain_making.gif_raw"

cwd = os.getcwd() 
os.chdir(cwd)
print(cwd) 

colors_coordination = {'0' : (0,0,0),'1' : (255,255,255),'2' : (128,128,128),'3' : (255,0,0),'4' : (255,128,0),'5' : (255,255,0),'6' : (0,255,0),'7' : (0,0,255),'8' : (128,0,255),'9' : (204,0,204)}

window = pyglet.window.Window(768,768) 
batch =  pyglet.graphics.Batch()

def color_changer(colors_mat,frame): 
    '''
    colors : 2d array with color data 
    frame = 
    '''
    
    window.clear() 
    circles = [] 
    r = 5
    spacing = 12

    # print(colors_mat[1])
          
    for i in range(64): 
        for j in range(64): 
            # print(colors_mat[i][j])
            
            c = colors_coordination[colors_mat[j][i]]
            # print(c) 
            circles.append(shapes.Circle(x=i*spacing+6,y=j*spacing+6,radius=r,color=c,batch=batch))
            
        
    
    batch.draw()
    pyglet.image.get_buffer_manager().get_color_buffer().save(f'{cwd}/image_cache/frame{frame}.png')

    
        

@window.event
def on_draw(): 

    with open(filename,'r') as f: 
        lines = f.read()
    lines = lines.split('\n')


    frame_number = (len(lines))/65 
    for i in range(int(frame_number)): 
        frame = int(lines[i*65])
        colors = lines[((i*65)+1):65*(i+1)]
        colors = [values.split(' ')[0:64] for values in colors]
        # print(frame[0]) 
        print(len(colors)) 
        color_changer(colors,frame)
        
        
    window.close()
        
    
    
    


pyglet.app.run()
