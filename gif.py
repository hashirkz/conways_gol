import os
import imageio.v2 as imageio

imgs_dir = r'./.frames'
images = [imageio.imread(os.path.join(imgs_dir, png)) for png in sorted(os.listdir(imgs_dir))]
imageio.mimsave('aya.gif', images)