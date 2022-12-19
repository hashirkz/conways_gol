import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from board import board

# app for conways game of life
# ctrl c to stop the program lol somtimes u have to keep doing it... 
def app():
    # make a new board from whatever data *img or csv in this case img
    brd = board(board.img_to_board('./imgs/aya.jpg', board_w = 70))

    # game loop
    plt.ion()
    while True:
        brd.show(time=0.1)
        brd.update()
        
app()


