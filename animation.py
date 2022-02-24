from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('dark_background')


class Animation:

    def __init__(self, *objs):
        """Initializes the animation class.
        INPUTS:
            objs - An arbitrary amount of objects to animate.
        """

        self.frames = []
        self.objs = objs

        self.frame()

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

        self.frames.append((fig, ax))
        plt.show()
        plt.close('all')
