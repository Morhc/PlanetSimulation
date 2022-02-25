import os
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image

plt.style.use('dark_background')

class Animation:

    def __init__(self, *objs):
        """Initializes the animation class.
        INPUTS:
            objs - An arbitrary amount of objects to animate.
        """

        self.savefolder = "PlanetSim"
        self.frame = 0

        self.objs = objs

        self.check_dir()
        self.frame()


    def check_dir(self):
        here = os.path.dirname(os.path.realpath(__file__))
        save = os.path.join(here, self.savefolder)

        if not os.path.isdir(save):
            os.makedir(save)

        self.savefolder = save

    def frame(self):
        #https://stackoverflow.com/questions/22566284/matplotlib-how-to-plot-images-instead-of-points

        AU = 1.496e11
        Rsun = 696e6

        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(111, projection='3d')

        hide = (0, 0, 0, 0)
        ax.w_xaxis.set_pane_color(hide)
        ax.w_yaxis.set_pane_color(hide)
        ax.w_zaxis.set_pane_color(hide)
        ax.w_xaxis.line.set_color(hide)
        ax.w_yaxis.line.set_color(hide)
        ax.w_zaxis.line.set_color(hide)

        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])

        for obj in self.objs:
            ax.scatter(obj.position[0]/AU, obj.position[1]/AU, obj.position[2]/AU, color = obj.colour, s = 2000*obj.radius/Rsun)

        plt.savefig(os.path.join(self.savefolder, f'anim_{self.frame}.png'))
        plt.close('all')

        self.frame += 1

def animate(self):

    fp_out = os.path.join(self.savefolder, "PlanetSim.gif")

    files = os.listdir(self.savefolder) if file.endswith('.png')
    img, *imgs = [Image.open(file) for file in files]
    img.save(fp=fp_out, format='GIF', append_images=imgs,
             save_all=True, duration=len(files)*70, loop=0)

    for file in files: os.remove(file)
