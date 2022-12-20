import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from board import board


# app for conways game of life
# ctrl c to stop the program lol somtimes u have to keep doing it... 
def app(save_gif: bool = False, time: int | None = None):

    # make a new board from whatever data *img or csv in this case img
    brd = board(board.img_to_board('./imgs/aya.jpg', 70))

    # game loop
    frames = 0 
    plt.ion()
    while True:
        brd.show(time=time, save_frame=save_gif, path=f'./.frames/img_{frames}.png')
        brd.update()
        frames += 1
    
        
app()


