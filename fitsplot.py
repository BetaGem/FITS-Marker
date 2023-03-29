from astropy.io import fits 
from io import BytesIO
from os import listdir
import numpy as np
import base64

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.colors import SymLogNorm
from scipy.signal import convolve2d
from astropy.visualization import make_lupton_rgb

fpath = "data/fits_images"  # fits 图像所在的目录
h_1D = np.mat([[1.0/16,1.0/4,3.0/8,1.0/4,1.0/16]])
Kernel = np.mat([[1.0/16],[1.0/4],[3.0/8],[1.0/4],[1.0/16]])*h_1D

def search_fits(n):
    '''从目录搜索第 n 个图像并且返回文件名'''
    f = 2
    for f_name in listdir(fpath):
        if f_name.startswith(str(n)+'-'):
            f = f_name
            break
    return f

def print_fig(fig):
    # Convert plot to PNG image
    pngImage = BytesIO()
    FigureCanvasAgg(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return pngImageB64String

def plot(k, band, style, con=0):
    dic = {1:'g', 2:'r', 3:'i'} # 三个波段
    # load data
    fits_name = search_fits(int(3*k) + int(band) - 2)
    hdul = fits.open(str(fpath)+str(fits_name))
    if con:
        # 是否对图像进行平滑
        img = convolve2d(hdul[1].data,Kernel,mode="same")
    else:
        img = hdul[1].data
    
    fig = Figure()
    min_c = style[0]
    max_c = style[1]
    ax = fig.add_subplot(1,1,1)
    ax.axis('off')
    # Figure.suptitle(fig,' '+str(dic[band])+' band',fontsize='xx-large')  # title
    fig.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    ax.imshow(img, 
              cmap='gray',
              aspect='auto', 
              norm=SymLogNorm(linthresh=0.3, linscale=1, 
                              vmin=min_c, vmax=max_c),
              origin="lower"
              )
    
    return print_fig(fig)
    
#def RGB(k,sty):
#    stretch = 2 / (int(sty) + 3)**2
#    fits_names = [''] * 3
#    hduls = [None] * 3
#    for band in range(3):
#        fits_names[band] = search_fits(int(3*k) + band - 1)
#        hduls[band] = fits.open(str(fpath)+str(fits_names[band]))
#
#    image = make_lupton_rgb((hduls[2])[1].data,
#                            convolve2d((hduls[1])[1].data, Kernel, mode="same"),
#                            convolve2d((hduls[0])[1].data, Kernel, mode="same"),
#                            minimum=-0,
#                            stretch=stretch,
#                            Q=10-int(sty)*1.5)
#    
#    fig = Figure()
#    ax = fig.add_subplot(1,1,1)
#    ax.axis('off')
#    fig.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
#    ax.imshow(image,aspect='auto')
#    return print_fig(fig)
