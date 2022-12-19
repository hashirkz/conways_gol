import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from skimage import transform
import scipy.ndimage as spimg

class board:
    def __init__(self, tensor:np.ndarray, dimensions: tuple | None = None):
        self.tensor = tensor
        self.dimensions = tensor.shape if not dimensions else dimensions

    # reset the current board
    def reset(self):
        self.tensor, self.dimensions = np.empty((0, 0)), (0, 0)


    # function to b&w img and scale img to board_w *default 200px
    @staticmethod
    def img_to_board(img_path: str, board_w: int = 200):
        try:
            img = mpimg.imread(img_path)

            # aspect ratio is board_w / img_w
            aspect_ratio = board_w / img.shape[1]
            img = board.rgb2gray(transform.rescale(img, aspect_ratio, multichannel=True))
            
            img_bool = (img > 0.25).astype(np.int)

            return img_bool

        except FileNotFoundError:
            return f'unable to find *{img_path}* in the current directory'

    # load board.tensor from a csv
    @staticmethod
    def csv_to_board(csv_path: str, board_w: int = 200):
        try:
            tensor = pd.read_csv(csv_path).to_numpy()

            # aspect ratio is board_w / img_w
            aspect_ratio = board_w / tensor.shape[1]
            tensor = board.rgb2gray(transform.rescale(tensor, aspect_ratio, multichannel=True))
            
            tensor_bool = (tensor > 0.25).astype(np.int)

            return tensor_bool

        except FileNotFoundError:
            return f'unable to find *{csv_path}* in the current directory'

    
    # convert rgb to gray scale *default function from matlab
    @staticmethod
    def rgb2gray(rgb:np.ndarray):
        r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
        gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

        return gray
    
    # void/inplace update the board based on conways game of life rules 
    def update(self):
        rows, cols = self.dimensions
        directions = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1)]
        for i in range(rows):
            for j in range(cols):

                # find number of surrounding inbound w and b pixels *ie convolve 3x3 matrix around i, j excluding i, j
                px, num_w, num_b = self.tensor[i][j], 0, 0
                for x, y in directions:
                    if 0 <= i + x < rows and 0 <= j + y < cols:
                        if self.tensor[i+x][j+y] == 1: 
                            num_w += 1
                        else: 
                            num_b += 1

                # w px and less than 2 or more than 3 surrounding w px
                if px == 1 and (num_w < 2 or num_w > 3): self.tensor[i][j] = 0
                elif px == 0 and num_w == 3: self.tensor[i][j] = 1

            
                
        # maybe just use 2d convolution with kernel
        # self.tesnor = spimg.convolve(self.tensor, np.ones((3, 3)))
        # key = lambda x : 0 if x == 1 and (x < 2 or x > 3) else 1

    # show the graph for the current board *need to use plt.ion() before using board.show(...)
    def show(self, time: int = 0.01):
        plt.imshow(self.tensor, cmap='gray')
        plt.draw()
        plt.pause(time)
        plt.clf()

    # save the current board to a csv
    def to_csv(self, path):
        df = pd.DataFrame(self.tensor)
        df.to_csv(path)

    # return pretty print representation for board
    def __str__(self):
        repr = ''
        for r in self.tensor:
            for c in r:
                repr += f'{c:3}'
            repr += '\n'

        return repr


if __name__ == '__main__':
    pass
    # testing stuff
    # aya = board(board.img_to_board('./imgs/aya.jpg', 70))
    # aya.show()
    # aya.to_csv('./data/aya.csv')

